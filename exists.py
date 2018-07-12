#!/usr/bin/python3

import os
import sys

def main():
    args = sys.argv
    # Checking if there even is a command-linx argument
    try:
        args[1]
    except IndexError:
        print("exists.py [path-to-file]")
        sys.exit(1)
    sfile = str(args[1])
    # Help argument
    if str(args[1]) == "-h":
        print("exists.py [path-to-file]")
        sys.exit(1)
    # Checks if file exists (LOL)
    if not os.path.isfile(sfile):
        print("Doesn't exist!")
    else:
        print("It exists!")
if __name__ == "__main__":
    main()