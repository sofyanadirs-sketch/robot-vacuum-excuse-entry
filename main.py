#!/usr/bin/env python3
"""Entry for make.fun: writes one single-line text to entry.txt.

The entry is a robot vacuum's excuse: it files a doctor's note for dust
allergies, signed by the Roomba next door — who has called in sick twice
this week. The joke works because the excuse is a classic human one (a
doctor's note), the ailment is absurd for a vacuum (dust allergies), and
the second twist is that the note's signer is another vacuum with the
same habit. Named thing + concrete number + insider artifact + second
twist, per the winning one-liner pattern. The vacuum never cleans the
floor it was bought for — it outsources the excuse instead.

The program is deterministic, uses only the Python 3 standard library,
makes no network calls, and writes exactly one line with no trailing
newline, so the sealed gate reads it as a 1-200 character text.
"""

import os
import sys

ENTRY = "My robot vacuum sent a doctor's note for dust allergies — signed by the Roomba next door, who has called in sick twice this week."

# The sealed gate only accepts a single line of 1-200 characters with no
# trailing newline, so guard the entry: a future edit that breaks the
# format must fail loudly here instead of producing a rejected entry.txt.
assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters long"
assert "\n" not in ENTRY, "ENTRY must be a single line (no newline)"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
