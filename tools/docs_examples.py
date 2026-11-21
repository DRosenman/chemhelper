"""Run every ``>>>`` example in the docs and README, and check or rewrite its output.

    python tools/docs_examples.py           # check; exit 1 if any output is stale
    python tools/docs_examples.py --write   # rewrite the outputs in place

Examples live in fenced ``pycon`` blocks. Each file gets one fresh namespace, so
an import in the first block of a page is visible in the blocks below it. A blank
line directly before a ``>>>`` line is kept as a separator; everything else that
is not input is treated as output and regenerated.
"""

import argparse
import contextlib
import io
import pathlib
import re
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

OPEN = re.compile(r"^(\s*)```pycon\s*$")


def run_block(lines, namespace):
    """Execute the statements in one block and return the block's new lines."""
    out = []
    i = 0
    while i < len(lines):
        if not lines[i].startswith(">>>"):
            i += 1
            continue
        if out and lines[i - 1].strip() == "":
            out.append("")
        shown = [lines[i]]
        source = [lines[i][4:]]
        i += 1
        while i < len(lines) and lines[i].startswith("..."):
            shown.append(lines[i])
            source.append(lines[i][4:])
            i += 1
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            try:
                exec(compile("\n".join(source) + "\n", "<docs>", "single"), namespace)
            except Exception as error:  # shown to the reader, like a real session
                print("Traceback (most recent call last):\n  ...")
                print("".join(traceback.format_exception_only(type(error), error)), end="")
        out.extend(shown)
        out.extend(line.rstrip() for line in buffer.getvalue().rstrip("\n").splitlines())
    return out


def process(text):
    namespace = {"__name__": "__docs__"}
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        match = OPEN.match(lines[i])
        result.append(lines[i])
        i += 1
        if not match:
            continue
        indent = match.group(1)
        block = []
        while i < len(lines) and lines[i].strip() != "```":
            block.append(lines[i][len(indent):])
            i += 1
        result.extend((indent + line).rstrip() for line in run_block(block, namespace))
    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--write", action="store_true", help="rewrite outputs in place")
    args = parser.parse_args()

    files = [ROOT / "README.md"] + sorted((ROOT / "docs").rglob("*.md"))
    stale = []
    for path in files:
        old = path.read_text(encoding="utf-8")
        new = process(old)
        if new != old:
            stale.append(path.relative_to(ROOT))
            if args.write:
                path.write_text(new, encoding="utf-8", newline="\n")
    if stale and not args.write:
        print("Example output is out of date in:")
        for path in stale:
            print("  ", path)
        print("Run: python tools/docs_examples.py --write")
        return 1
    print("{} file(s) {}.".format(len(stale) if args.write else len(files),
                                  "rewritten" if args.write else "checked, all examples up to date"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
