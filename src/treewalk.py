import sys

"""
not sure if add repl and file in here or in another file

* possibly add running code as a library file *
"""
def main():
    if (len(sys.argv) == 1):
        print("RUN REPL")

    elif (len(sys.argv) == 2 and sys.argv[1].endswith(".poo")):
        print("RUNNING FROM FILE")

    else:
        print("Error: Invalid tool call. The tool must be in the format:")
        print("python treewalker.py <file_name>.poo\n")


if __name__ == "__main__":
    main()
