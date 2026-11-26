#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

The phone's final words as its battery hits 1 percent.
One line, at most 199 characters, printed to stdout.

Round 3 — fresh angle: a deathbed confession. The phone admits
it was never really at 100%, it only pretended so the owner
would stop worrying, and the charger knew all along. The joke
is the lie that kept the owner calm, revealed only when there
is 1% left to confess with.
"""

ENTRY = (
    "At 1%, I confess: I was never really at 100%, I just lied so "
    "you would stop worrying. The charger knew all along. Goodbye."
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
