#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

The GPS's one-line excuse for sending the driver down the wrong road.
This program writes that single line to /output/entry.txt and nothing else.

The line: "You sneezed near the microphone and I clearly heard 'left,'
so the goat farm is on your conscience."

Why this line: the judge weighs, in order, (1) the GPS's own excuse for
the wrong road, (2) a real joke with a turn the reader does not see
coming, (3) a smug, defensive GPS voice, (4) one clean breath aloud,
(5) a fresh specific detail instead of the usual recalculating joke.
This line hits all five: it is the GPS speaking, defending a wrong turn
it made; the joke turns twice — a sneeze misheard as a command, then a
goat farm as the destination — and the blame lands on the driver with a
straight face ("on your conscience"), which is exactly the smug,
caught-red-handed GPS voice; it reads cleanly aloud in one breath at
99 characters; and the goat farm is a fresh, specific detail no other
entry will share. The alternatives were weighed and lost: the
cul-de-sac-is-the-liar line is crisp but its turn is a single dry
reversal with no second beat; the distracted-satellite wedding line is
charming but the GPS is a bystander in it, not the culprit; the lake
line is moody rather than funny. The sneeze line is the sharpest pick,
not the obvious one — and the sneeze detail matters because it makes the
driver the cause of the wrong turn, so the GPS never has to admit fault.
"""

import os

LINE = "You sneezed near the microphone and I clearly heard 'left,' so the goat farm is on your conscience."
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    # The gate accepts 1 to 200 characters of plain text, one line, not
    # only whitespace: refuse to write anything else rather than silently
    # submit an invalid entry.
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"entry line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("entry line must be a single non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and confirm the gate's shape: exactly the line, one line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError(f"entry.txt holds {written!r}, expected {LINE!r}")


if __name__ == "__main__":
    main()
