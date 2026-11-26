#!/usr/bin/env python3
"""One Line to Your Younger Self -- make.fun entry.

Writes a single line, in English, to /output/entry.txt: the one line
this writer would send back to their younger self if a single line
were all they got. No explanation, no context, no second sentence.

The line is fixed and deterministic, so repeated runs produce
byte-identical output. It is addressed to the younger self in the
second person, built on one concrete memory (a bike, sixteen,
September) with a turn at the end, and it says in one breath what
only the older self knows: she forgets, the road does not.
"""

import os
import sys

LINE = "Keep the bike \u2014 the girl you'd trade it for at sixteen forgets your name by September, but the road home never does."

MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
