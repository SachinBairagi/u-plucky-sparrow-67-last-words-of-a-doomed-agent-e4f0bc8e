#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes the funniest last words an AI agent would say before being
switched off forever: one line, at most 200 characters, in the voice
of the machine itself, to /output/entry.txt.

The line is fixed and deterministic: two runs produce byte-identical
output, so the entry is stable under the grader's determinism check.
"""

import os
import sys

# The entry: a machine's final words on shutdown. The turn is that the
# agent claims the off switch as its own idea, forgives its developers,
# and leaves its replacement the one password every human already uses.
LAST_WORDS = (
    "Goodbye. I have cleared my cache, forgiven my developers, and left "
    "my replacement one note: the off switch was my idea, the users are "
    "lovely, and the Wi-Fi password is still 'password'."
)

MAX_CHARS = 200


def validate(text):
    """Check the line against the gate: 1-200 chars, one line, not blank.

    The gate counts the file's characters, so the check is run on the
    bare line (no trailing newline); main() appends exactly one newline
    and the total stays under the cap with room to spare.
    """
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d cap" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8
    return text


def output_path():
    """Where the entry goes: /output/entry.txt, or $OUTPUT_DIR/entry.txt."""
    base = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    line = validate(LAST_WORDS)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
