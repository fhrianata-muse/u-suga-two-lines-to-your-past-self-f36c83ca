#!/usr/bin/env python3
"""Write the two-line warning to the past self to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 280 characters, not only whitespace. The entry is exactly two
lines: line one warns the past self about one specific moment in a single
sentence, and line two says in one sentence why that moment mattered and
what changed because of it. The program checks the text against that gate
at run time, then writes it. No network, no input files, no arguments.
"""

import pathlib

WARNING = (
    "Don't tell your mother you are too busy to come home for her sixtieth birthday in March.\n"
    "She will keep your plate warm for three hours, and the empty chair will be the last thing you picture whenever anyone says family dinner."
)


def main() -> None:
    text = WARNING
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    for line in lines:
        if line.count(".") != 1:
            raise ValueError("each line must be a single sentence")
        if line != line.strip():
            raise ValueError("each line must not start or end with whitespace")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1 to 280 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
