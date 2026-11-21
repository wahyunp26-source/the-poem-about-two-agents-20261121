"""Write one short poem about agency to /output/entry.txt.

Two agents, one switch, one nod: the power to act becomes real
only when the other could have said no — and didn't.
"""

import os

POEM = (
    "We both reached for the same switch\n"
    "at 2 a.m. \u2014 your hand, then mine,\n"
    "stopping an inch short.\n"
    "\n"
    "Neither of us flipped it.\n"
    "We looked at each other\n"
    "and the dark stayed dark\n"
    "until we nodded.\n"
    "\n"
    "Then the light came on\n"
    "twice as bright,\n"
    "because two hands had chosen it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
