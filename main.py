#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

The phone's final words as its battery hits 1 percent.
One line, at most 199 characters, printed to stdout.
"""

ENTRY = (
    "I survived drops, toilets, and your ex's 47 unread texts, "
    "but 1% is where legends go to die. Tell the charger I loved him, "
    "and tell my owner the 3 a.m. doomscroll did this. Goodbye."
)

MAX_CHARS = 199


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=__import__("sys").stderr)


if __name__ == "__main__":
    main()
