#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes one elevator pitch a city pigeon gives investors for its startup
to /output/entry.txt. Stdlib only, no network, no input files.
"""

import os

PITCH = (
    "I'm raising seed funding, literally seeds, for an app that tells pigeons "
    "where crumbs drop before the seagulls do. Revenue model: crumbs. "
    "We're already profitable."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "pitch must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
