"""Write one childhood-memory sentence to /output/entry.txt.

Stdlib only, deterministic, no input, no network, no randomness.
"""

import os

ENTRY = "On summer evenings my grandmother would lift me onto a chair to stir the tomato sauce, steam fogging my glasses while she hummed off-key, and even now a kitchen that smells like that puts me back on that chair."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
