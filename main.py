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

MAX_CHARS = 200


def validate(line: str) -> str | None:
    """Return an error message if the line breaks the gate, else None."""
    if not line or not line.strip():
        return "line is empty or only whitespace"
    if len(line) > MAX_CHARS:
        return f"line is {len(line)} characters, expected 1-{MAX_CHARS}"
    if "\n" in line or "\r" in line:
        return "line must be a single line (no newline characters)"
    return None


def main() -> int:
    error = validate(LINE)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip() or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        # Round-trip check: what landed on disk must be exactly the line,
        # valid UTF-8, still one line.
        with open(path, "r", encoding="utf-8", newline="") as f:
            written = f.read()
    except OSError as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 1
    if written != LINE:
        print("written entry does not match the line", file=sys.stderr)
        return 1

    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
