#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review (one line, <=160 chars) of an
everyday essential to /output/entry.txt.

Candidates considered (fresh angles, different essentials):
  1. Sleep:    "I sleep eight hours a night and still wake up tired, as if
                sleep charges everyone else and leaves me on 1%."
  2. The sun:  "The sun is up before me, gone before dinner, and still
                manages to burn me through a window on my day off."
  3. Monday:   "Monday arrives every week without fail, which is the only
                thing about it that has ever been reliable."

Picked #1 (sleep): the sharpest true grievance — everyone recognises
waking up tired after a full night's sleep, yet nobody has filed the
complaint in earnest. Deadpan throughout, no exclamation marks, and the
turn lands in the last few words ("leaves me on 1%"), recasting
sleep as a charger that works for everyone except the reviewer.
"""

import os

ENTRY = (
    "I sleep eight hours a night and still wake up tired, "
    "as if sleep charges everyone else and leaves me on 1%."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
