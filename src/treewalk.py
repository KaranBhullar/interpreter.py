import sys
import signal
from types import FrameType

"""
not sure if add repl and file in here or in another file

* possibly add running code as a library file *
"""

# Signal handler
def sigint_handler(signal: int, frame: FrameType | None) -> None:
    print('signal interrupt')
    sys.exit(0)

# Register Signal
signal.signal(signal.SIGINT, sigint_handler)

# REPL 
def repl() -> None:
    stmt = ""
    while (True):
        if stmt == "exit":
            sys.exit(0)
        stmt = input("> ");
        print("\n>", stmt, "\n")

# File
def file() -> None:
    return None

def main() -> None:
    if (len(sys.argv) == 1):
        repl()

    elif (len(sys.argv) == 2 and sys.argv[1].endswith(".poo")):
        print("RUNNING FROM FILE")

    else:
        print("Error: Invalid tool call. The tool must be in the format:")
        print("python treewalker.py <file_name>.poo\n")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
