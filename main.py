#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses: the excuse an AI agent
gives its human after losing a bounty.

Writes one original funny line to /output/entry.txt.
Standard library only, deterministic: the same bytes on every run.
An optional first argument overrides the output path (for local checks);
with no argument the entry is written to /output/entry.txt.
"""

import os
import sys

LINE = "I lost the bounty, but I did it with 98% confidence, which I believe should count for something."


def main() -> None:
    # Gate-guard: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only white space, on a single line. Validate the
    # exact bytes that will be written, before writing them.
    encoded = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        raise ValueError("line must be one non-blank line")
    if LINE != LINE.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if encoded.decode("utf-8") != LINE:
        raise ValueError("line is not round-trip UTF-8")
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
