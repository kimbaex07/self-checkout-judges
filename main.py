#!/usr/bin/env python3
"""Write this entry's one-line self-checkout remark to /output/entry.txt.

Pure Python standard library only. The line is the whole entry:
one funny line in the voice of a smug self-checkout machine.
"""

import os

LINE = "One tomato, one candle, no bag. Even I can tell you're not cooking dinner — you're apologising to someone."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Gate: the entry must be one line, 1-200 characters, no padding.
    # The grader reads /output/entry.txt; keep it exactly one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
