import sys
import signal
import os.path
from types import FrameType
from scanner import Scanner
"""
* possibly add running code as a library file *

REPL AND FILE RUNNING SHOULD BE IN SEPARATE FILES
-> SHOULD HANDLE SIGNALS ACCORDINGLY
"""

# Error handlers | CHANGE THIS TO BE BETTER
class FileNotFoundError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Signal handler
def sigint_handler(signal: int, frame: FrameType | None) -> None:
    print('Keyboard Interrupt')

def EOF_handler(signal: int, frame: FrameType | None) -> None:
    sys.exit(0)

# Register Signal
signal.signal(signal.SIGINT, sigint_handler)
# signal.signal(signal, EOF_handler)

# REPL 
def repl() -> None:
    stmt = ""
    while (True):
        stmt = input("> ");
        if stmt == "exit":
            sys.exit(0)
        run(stmt)

        print(">", stmt) # TEMPORARY

def file(path: str) -> None:
    if not os.path.isfile(path):
        print('working')
        raise FileNotFoundError("File missing brother")

    with open(path, "r") as f:
        run(f.read())
        f.close()

    return None

def run(src: str) -> None:
    scanner = Scanner(src)
    tokens = scanner.scan()
    for token in tokens:
        print(token)

def main() -> None:
    if (len(sys.argv) == 1):
        repl()

    elif (len(sys.argv) == 2 and sys.argv[1].endswith(".fsh")):
        print("RUNNING FROM FILE\n")
        file(sys.argv[1])

    else:
        print("Error: Invalid tool call. The tool must be in the format:")
        print("python treewalker.py <file_name>.poo\n")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
