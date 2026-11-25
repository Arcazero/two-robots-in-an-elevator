#!/usr/bin/env python3
"""Two Robots in an Elevator.

Writes one funny line of awkward small talk that one robot says to
another while they ride an elevator together, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

LINE = (
    "Forty-seven rides in this elevator, and I know your firmware, "
    "your battery level, and your last 200 locations \u2014 but asking "
    "your name felt too personal."
)


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} characters, expected 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
