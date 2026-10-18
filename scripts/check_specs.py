#!/usr/bin/env python3
"""Check Mothlight's current Markdown contract structure using only the stdlib.

Run from any working directory. This checks files, local links, stable IDs and the
current work table; it does not verify runtime behavior, approval or semantics.
It supports ordinary inline/reference Markdown links and GitHub-style headings,
not a complete CommonMark/HTML renderer. Archived definitions are not re-scanned.
"""

from __future__ import annotations

import html
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SPEC_NAMES = (
    "00_PROJECT_INTAKE.md", "01_PROJECT_CONTEXT.md", "02_STRATEGIC_PLAN.md",
    "03_MASTER_PRODUCTION_SPEC.md", "04_CLAUDE_CODE_BUILD_PROMPT.md",
    "05_BUILD_REVIEW.md", "06_PATCH_PLAN.md", "07_KNOWN_GAPS.md",
    "08_CHANGELOG_AI.md", "DECISION_LOG.md", "UI_REFERENCE.md",
    "DATA_REGISTRY.md", "MODEL_REGISTRY.md",
)
CORE = ("README.md", "AGENTS.md", "CLAUDE.md") + tuple(
    f"specs/{name}" for name in SPEC_NAMES
)
PR_TEMPLATE = ".github/pull_request_template.md"
ID_PATTERN = r"ML-(?:[WDGP]\d{3}|(?:GOV|DATA|HOST|WEB|MAIL|OBS|OPS|VER|UI)-\d{3})"
IDS = re.compile(rf"(?<![\w-]){ID_PATTERN}(?![\w-])")
DEFINITION = re.compile(rf"^#{{2,6}} ({ID_PATTERN})\s*$")
WORK_ID = re.compile(r"ML-W\d{3}")
STATES = {"planned", "in_progress", "blocked", "implemented", "verified", "released"}
DEPLOYMENTS = {"not_applicable", "not_deployed", "deployed"}
OWNERS = {
    "W": "02_STRATEGIC_PLAN.md", "D": "DECISION_LOG.md",
    "G": "07_KNOWN_GAPS.md", "P": "06_PATCH_PLAN.md",
    "GOV": "04_CLAUDE_CODE_BUILD_PROMPT.md", "UI": "UI_REFERENCE.md",
}
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.*?)\s*#*\s*$")
LABEL = r"(?:\\.|[^\]\\])*"
INLINE_LINK = re.compile(rf"!?\[{LABEL}\]\(")
REF_DEFINITION = re.compile(rf"^ {{0,3}}\[({LABEL})\]:\s*(.*)$")
REF_LINK = re.compile(rf"!?\[({LABEL})\](?:\[({LABEL})\])?")


def without_fences(text: str) -> str:
    """Preserve line numbers while excluding backtick and tilde fenced blocks."""
    output, opened = [], None
    for line in text.splitlines():
        match = FENCE.match(line)
        if opened:
            if (match and match[1][0] == opened[0]
                    and len(match[1]) >= opened[1] and not match[2].strip()):
                opened = None
            output.append("")
        elif match:
            opened = (match[1][0], len(match[1]))
            output.append("")
        else:
            output.append(line)
    return "\n".join(output)


def destination(text: str, start: int = 0) -> tuple[str, int]:
    """Read a Markdown destination, including escaped/balanced parentheses."""
    pos = start
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos < len(text) and text[pos] == "<":
        end = text.find(">", pos + 1)
        return (text[pos + 1:end], end + 1) if end >= 0 else ("", pos)
    begin, depth = pos, 0
    while pos < len(text):
        char = text[pos]
        if char == "\\" and pos + 1 < len(text):
            pos += 2
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
        elif char.isspace() and depth == 0:
            break
        pos += 1
    return text[begin:pos], pos


def reference_key(label: str) -> str:
    return " ".join(label.split()).casefold()


def links(text: str) -> list[tuple[int, str]]:
    """Find destinations in ordinary inline links and defined reference links."""
    lines = text.splitlines()
    references, found = {}, []
    for number, line in enumerate(lines, 1):
        match = REF_DEFINITION.match(line)
        if match:
            target, _ = destination(match[2])
            references[reference_key(match[1])] = target
            found.append((number, target))
    for number, line in enumerate(lines, 1):
        if REF_DEFINITION.match(line):
            continue
        occupied = []
        for match in INLINE_LINK.finditer(line):
            target, end = destination(line, match.end())
            found.append((number, target))
            occupied.append((match.start(), end))
        for match in REF_LINK.finditer(line):
            if any(begin <= match.start() < end for begin, end in occupied):
                continue
            label = match[2] or match[1]
            target = references.get(reference_key(label))
            if target is not None:
                found.append((number, target))
    return found


def anchors(text: str) -> set[str]:
    """Approximate GitHub heading slugs; include explicit HTML id/name anchors."""
    result, used = set(), set()
    for match in re.finditer(r"<[^>]+\b(?:id|name)=[\"']([^\"']+)[\"'][^>]*>", text):
        result.add(html.unescape(match[1]))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = HEADING.match(line)
        title = match[1] if match else None
        if (title is None and index and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line)
                and lines[index - 1].strip()):
            title = lines[index - 1].strip()
        if title is None:
            continue
        title = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", title)
        title = html.unescape(re.sub(r"<[^>]*>", "", title)).strip().lower()
        slug = "".join(char for char in title if (
            char in "_- " or unicodedata.category(char)[0] in "LNM"
        )).replace(" ", "-")
        candidate, suffix = slug, 0
        while candidate in used:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        used.add(candidate)
        result.add(candidate)
    return result


def check(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    errors: list[str] = []
    counts = {"documents": 0, "local_links": 0, "definitions": 0,
              "id_references": 0, "work_rows": 0}
    texts: dict[Path, str] = {}

    def read(path: Path) -> str | None:
        if path in texts:
            return texts[path]
        try:
            path.resolve().relative_to(root)
        except (ValueError, OSError, RuntimeError):
            errors.append(f"{path.relative_to(root)}: file escapes project root")
            return None
        try:
            text = without_fences(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(root)}: cannot read ({exc})")
            return None
        texts[path] = text
        return text

    current = []
    for name in (*CORE, PR_TEMPLATE):
        path = root / name
        if not path.is_file():
            errors.append(f"{name}: required file missing")
        elif read(path) is not None:
            current.append(path)
    agents = texts.get(root / "AGENTS.md", "")
    if root / "AGENTS.md" in current and "CLAUDE.md" not in agents:
        errors.append("AGENTS.md: must point to CLAUDE.md")

    # Evidence can link back to contracts, but cannot define or change current IDs.
    evidence = sorted((root / "specs" / "evidence").rglob("*.md"))
    documents = current + [path for path in evidence if read(path) is not None]
    counts["documents"] = len(documents)
    for source in documents:
        for number, raw in links(texts[source]):
            location = f"{source.relative_to(root)}:{number}"
            raw = html.unescape(re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])", r"\1", raw))
            try:
                url = urlsplit(raw)
            except ValueError:
                errors.append(f"{location}: invalid link {raw!r}")
                continue
            if url.scheme.lower() in {"http", "https", "mailto"} or url.netloc:
                continue
            if url.scheme:
                errors.append(f"{location}: unsupported local-link scheme {url.scheme!r}")
                continue
            counts["local_links"] += 1
            try:
                target = (source.parent / unquote(url.path)).resolve() if url.path else source.resolve()
                target.relative_to(root)
            except (ValueError, OSError, RuntimeError):
                errors.append(f"{location}: link escapes project root: {raw!r}")
                continue
            if not target.exists():
                errors.append(f"{location}: missing link target {raw!r}")
                continue
            if url.fragment:
                target_text = read(target) if target.is_file() else None
                if target_text is None or unquote(url.fragment) not in anchors(target_text):
                    errors.append(f"{location}: missing anchor in {raw!r}")

    definitions: dict[str, list[tuple[Path, int]]] = {}
    references: dict[str, list[tuple[Path, int]]] = {}
    for source in current:
        for number, line in enumerate(texts[source].splitlines(), 1):
            match = DEFINITION.fullmatch(line)
            if match:
                identity = match[1]
                definitions.setdefault(identity, []).append((source, number))
                namespace = identity[3:].split("-")[0]
                if namespace[0] in "WDGP" and namespace[1:].isdigit():
                    namespace = namespace[0]
                owner = "specs/" + OWNERS.get(namespace, "03_MASTER_PRODUCTION_SPEC.md")
                if source != root / owner:
                    errors.append(f"{source.relative_to(root)}:{number}: {identity} belongs in {owner}")
            for match in IDS.finditer(line):
                references.setdefault(match[0], []).append((source, number))
                counts["id_references"] += 1
    counts["definitions"] = len(definitions)
    for identity, occurrences in definitions.items():
        if len(occurrences) != 1:
            locations = ", ".join(f"{path.relative_to(root)}:{number}" for path, number in occurrences)
            errors.append(f"{identity}: duplicate definition ({locations})")
    for identity, occurrences in references.items():
        if identity not in definitions:
            path, number = occurrences[0]
            errors.append(f"{path.relative_to(root)}:{number}: undefined ID {identity}")

    work_rows: dict[str, int] = {}
    review = texts.get(root / "specs/05_BUILD_REVIEW.md", "")
    for number, line in enumerate(review.splitlines(), 1):
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        first_ids = WORK_ID.findall(cells[0])
        if not first_ids:
            continue
        identity = cells[0]
        if not WORK_ID.fullmatch(identity):
            errors.append(f"specs/05_BUILD_REVIEW.md:{number}: first work cell must be a plain ML-W ID")
            continue
        work_rows[identity] = work_rows.get(identity, 0) + 1
        counts["work_rows"] += 1
        if len(cells) != 5:
            errors.append(f"specs/05_BUILD_REVIEW.md:{number}: work row requires exactly five columns")
            continue
        if cells[1].strip("`") not in STATES:
            errors.append(f"specs/05_BUILD_REVIEW.md:{number}: invalid work state {cells[1]!r}")
        if cells[2].strip("`") not in DEPLOYMENTS:
            errors.append(f"specs/05_BUILD_REVIEW.md:{number}: invalid deployment state {cells[2]!r}")
        if not cells[3] or not cells[4]:
            errors.append(f"specs/05_BUILD_REVIEW.md:{number}: owner and evidence/dependency must be present")
    work_definitions = {identity for identity in definitions if WORK_ID.fullmatch(identity)}
    for identity in sorted(work_definitions | work_rows.keys()):
        if identity not in work_definitions:
            errors.append(f"specs/05_BUILD_REVIEW.md: row {identity} has no work definition")
        if work_rows.get(identity, 0) != 1:
            errors.append(f"specs/05_BUILD_REVIEW.md: {identity} needs one current row; found {work_rows.get(identity, 0)}")
    return errors, counts


def main() -> int:
    errors, counts = check(ROOT)
    print("Structural specs check: " + "; ".join(
        f"{value} {key.replace('_', ' ')}" for key, value in counts.items()
    ))
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{'FAIL: ' + str(len(errors)) + ' issue(s)' if errors else 'PASS'}. "
          "Structural only; runtime behavior and semantic acceptance are not assessed.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
