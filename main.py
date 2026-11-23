"""Write the two-line morning-light poem to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
/output. Standard library only; writes exactly the required text plus a single
trailing newline.
"""

import os

TEXT = "Morning slides a blade under the door,\nand my father's chair keeps his shape a while longer.\n"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)

if __name__ == "__main__":
    main()
