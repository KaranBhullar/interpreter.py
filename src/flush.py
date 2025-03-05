import sys
import os.path
from scanner import Scanner
from exception_handler import FileNotFoundError
"""
-> make module for exception handling (class)
-> 
"""
# REPL 
def repl() -> None:
    stmt = ""
    while (True):
        stmt = input("> ");
        if stmt == "exit":
            sys.exit(0)
        run(stmt)

def file(path: str) -> None:
    if not os.path.isfile(path):
        print('working')
        raise FileNotFoundError("File missing brother")

    with open(path, "r") as f:
        run(f.read())
        f.close()

    return None

# For now it scans the input outputs all of the tokens
def run(src: str) -> None:
    scanner = Scanner(src)
    scanner.scan()
    scanner.to_str()

def main() -> None:
    if (len(sys.argv) == 1):
        repl()

    elif (len(sys.argv) == 2 and sys.argv[1].endswith(".fsh")):
        print("RUNNING FROM FILE\n")
        file(sys.argv[1])

    else:
        print("Error: Invalid tool call. The tool must be in the format:")
        print("python treewalker.py <file_name>.fsh\n")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
