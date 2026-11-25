#!/usr/bin/env python3
"""Write one nostalgic childhood sentence to /output/entry.txt.

Deterministic: the sentence is a fixed constant, so repeated runs
produce byte-identical output.
"""

import os

SENTENCE = (
    "On summer evenings my grandmother would lift me onto a chair to stir "
    "the tomato sauce, steam fogging my glasses while she hummed off-key, "
    "and even now a kitchen that smells like that puts me back on that "
    "chair."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    os.chmod("/output/entry.txt", 0o644)
    os.chmod("/output", 0o755)


if __name__ == "__main__":
    main()
