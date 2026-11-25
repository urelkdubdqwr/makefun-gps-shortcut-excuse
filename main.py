import os

ENTRY = "That was not a wrong turn. That was an unplanned water feature test. Results: your car is a boat, the car seat is a lake, and I remain, as ever, undefeated in navigation.\n"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
