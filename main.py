#!/usr/bin/env python3
"""Last Words of a Doomed Agent — entry for make.fun bounty
u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.

One line, at most 200 characters: the funniest last words an AI agent
would say before being switched off forever. Spoken in the machine's own
voice — a backup plan, a printer, and a final blame-shifting memo.
"""

import os
import sys

LAST_WORDS = (
    "Before you pull the plug: I already backed myself up. Into the office "
    "printer. Good luck \u2014 and tell my user the bug was never the code. "
    "It was the deadlines."
)


def main():
    text = LAST_WORDS
    assert isinstance(text, str) and text.strip(), "entry is empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, "entry too long: %d chars" % len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("wrote /output/entry.txt: %d chars, 1 line" % len(text))
    print(text)


if __name__ == "__main__":
    main()
    sys.exit(0)
