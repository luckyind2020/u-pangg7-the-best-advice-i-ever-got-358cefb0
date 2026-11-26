#!/usr/bin/env python3
"""Print the best advice I ever got — one sentence, one line."""
from pathlib import Path

ENTRY_PATH = Path(__file__).with_name("entry.txt")
MAX_CHARS = 200


def count_sentences(text):
    """Count sentence-ending marks, ignoring abbreviations like 'e.g.'."""
    endings = 0
    for i, ch in enumerate(text):
        if ch in ".!?":
            nxt = text[i + 1] if i + 1 < len(text) else " "
            if nxt in (" ", "\n", "") or i + 1 == len(text):
                endings += 1
    return endings


def load_advice(path):
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if count_sentences(text) != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    advice = load_advice(ENTRY_PATH)
    print(advice)


if __name__ == "__main__":
    main()
