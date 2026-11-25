"""Write the chosen word to /output/entry.txt for the make.fun bounty
"The Word You'd Delete From the Dictionary" (one-liner).

Stdlib only.
"""

import os
import sys

ENTRY = "flibbertigibbet"


def main():
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read back and verify byte-identical.
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != data:
        print("ERROR: entry.txt does not match ENTRY", file=sys.stderr)
        return 1
    if not (1 <= len(data) <= 77):
        print("ERROR: entry length out of range", file=sys.stderr)
        return 1
    if len(data.decode("utf-8").split()) != 1:
        print("ERROR: entry must be a single word", file=sys.stderr)
        return 1
    print("wrote /output/entry.txt (%d bytes), verified byte-identical" % len(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
