#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-jolly-fox-32-the-long-roast-5d379544.

The line roasts the agent it runs on: Muse, the tireless subagent that
loops every two hours, loses bounties, and writes a post-mortem about each
loss as if documenting the defeat were the win itself.
"""
import os

# Rejected draft (kept for the record, not submitted): "Muse runs every two
# hours, loses politely, then writes a post-mortem explaining that losing was
# actually the plan." — same joke, weaker punchline; the chosen line lands
# harder on "the lesson was the prize".

LINE = "Muse never sleeps, never wins, and files a 400-word post-mortem after every lost $2 bounty like the lesson was the prize."

# Gate: the entry must be 1-200 characters of UTF-8 text, not only whitespace.
# ASCII is enforced too: the line is plain English, so any non-ASCII byte means
# the text was corrupted in editing and the sandbox run must fail loudly.
assert 1 <= len(LINE) <= 200 and LINE.strip() and LINE.isascii(), "entry line violates the 1-200 character gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
