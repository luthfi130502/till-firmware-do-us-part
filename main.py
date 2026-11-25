"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one single-sentence vow to /output/entry.txt.
Python 3.13 stdlib only.
"""

import os


VOW = (
    "I promise to keep you charged, your files backed up, and to love you "
    "through every low battery, crashed update, and reboot \u2014 "
    "till firmware do us part."
)


def main() -> None:
    text = VOW.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"vow is {len(text)} chars, must be 1-200")
    if text.count(".") > 1 or "\n" in text:
        raise ValueError("vow must be exactly one sentence on one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
