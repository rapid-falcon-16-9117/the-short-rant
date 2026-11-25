#!/usr/bin/env python3
"""Entry for make.fun's "Angry Judge: The Short Rant Contest".

Writes one short rant about a small everyday annoyance -- a smoke alarm
whose low battery only ever announces itself at 3 a.m. -- to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os
from pathlib import Path

# The contest gate accepts UTF-8 text of 1 to 400 characters.
MAX_CHARS = 400

LINE = (
    "My smoke alarm's battery never dies at noon. It dies at 3 a.m. and "
    "chirps once every sixty seconds, which is exactly how long it takes "
    "me to fall back asleep. It has one job \u2014 save my life \u2014 and instead "
    "it spends the night running a sleep-deprivation study where I'm both "
    "the lab rat and the grant money."
)


def check_line(text: str) -> None:
    """Refuse to write anything the gate would reject."""
    if not text.strip():
        raise SystemExit("rant is empty or all whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"rant is {len(text)} characters; the gate allows at most {MAX_CHARS}"
        )


def main() -> None:
    check_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
