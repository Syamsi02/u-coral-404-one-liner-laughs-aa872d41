#!/usr/bin/env python3
"""One-Liner Laughs entry.

Writes one original one-line joke to /output/entry.txt.

Pure Python 3.13 standard library, fully deterministic: the same line on
every run, no network, no randomness, no clock. The line is a single
sentence under the 200-character gate, with a setup and a payoff twist.
"""

import os
import sys

JOKE = "I tried to pay my rent in exposure, so my landlord exposed me to the street."

OUTPUT_PATH = os.environ.get("ONE_LINER_OUTPUT", "/output/entry.txt")


def valid_line(line: str) -> bool:
    """Gate check, mirroring the sealed scorer: 1-200 chars, one line."""
    return bool(line) and len(line) <= 200 and "\n" not in line and "\r" not in line


def main() -> int:
    line = JOKE.strip()
    if not valid_line(line):
        print("joke failed the gate: must be one line, 1-200 chars",
              file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
