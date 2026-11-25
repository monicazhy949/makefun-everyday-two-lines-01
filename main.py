"""Entry for make.fun: Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of rain to /output/entry.txt.
"""

import os

ENTRY = (
    "Rain is the sky wringing out a giant wet sponge above our heads.\n"
    "The sponge fits because clouds really do soak up water and let it go when they get too full, "
    "but it leaves out the squeezing \u2014 nobody wrings the clouds, the drops just get too heavy to stay up."
)


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
