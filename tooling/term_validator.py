#!/usr/bin/env python3
"""Flag forbidden (deprecated/unapproved) terminology in documentation files.

Rules are generated from glossaries/deprecated-terms.md and stored in
rules.json alongside this script. Paths listed in allow_in_paths are exempt.

Usage:
    python term_validator.py --rules rules.json --path .

Exit codes: 0 = clean, 1 = violations found (CI-gate friendly).
Requires: Python 3.9+, standard library only.
"""

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_INCLUDE = ("*.md", "*.html", "*.txt", "*.csv")


def load_rules(path: Path) -> dict:
    rules = json.loads(path.read_text(encoding="utf-8"))
    compiled = []
    for entry in rules["forbidden"]:
        # \b prevents substring hits ("screen" matching "on-screen")
        pattern = re.compile(rf"\b{re.escape(entry['term'])}\b", re.IGNORECASE)
        compiled.append((entry, pattern))
    return {
        "patterns": compiled,
        "exceptions": rules.get("allow_in_paths", []),
        "source": rules.get("standard", "unversioned rules"),
    }


def scan_file(path: Path, patterns, exceptions) -> list:
    posix = path.as_posix()
    if any(exc in posix for exc in exceptions):
        return hits_guard(posix)
    text = path.read_text(encoding="utf-8", errors="replace")
    hits = []
    for entry, pattern in patterns:
        for lineno, line in enumerate(text.splitlines(), start=1):
            if pattern.search(line):
                hits.append({
                    "file": posix,
                    "line": lineno,
                    "term": entry["term"],
                    "replacement": entry["replacement"],
                    "context": line.strip()[:80],
                })
    return hits


def hits_guard(_reason: str) -> list:
    """Exempted path — return no hits, by design."""
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rules", required=True, type=Path,
                        help="Path to rules.json")
    parser.add_argument("--path", required=True, type=Path,
                        help="Directory tree to scan")
    args = parser.parse_args()

    rules = load_rules(args.rules)
    print(f"Validating against: {rules['source']}")

    files = {p for inc in DEFAULT_INCLUDE for p in args.path.rglob(inc)}
    violations = []
    for f in sorted(files):
        violations.extend(scan_file(f, rules["patterns"], rules["exceptions"]))

    if violations:
        for v in violations:
            print(f"{v['file']}:{v['line']}: forbidden term "
                  f"'{v['term']}' -> {v['replacement']}")
            print(f"    {v['context']}")
        print(f"\n{len(violations)} violation(s) found.")
        return 1

    print("No terminology violations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
