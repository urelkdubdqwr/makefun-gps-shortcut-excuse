"""Write the GPS shortcut excuse to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, else /output.
"""

import os
import sys

ENTRY = "That was not a wrong turn. That was an unplanned water feature test. Results: your car is a boat, the car seat is a lake, and I remain, as ever, undefeated in navigation.\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        sys.stderr.write("cannot create output directory %r: %s\n" % (out_dir, exc))
        raise SystemExit(1)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
