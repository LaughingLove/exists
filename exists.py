#!/usr/bin/python3

import os
import sys

def main():
    args = sys.argv
    # Checking if there even is a command-linx argument
    try:
        args[1]
    except IndexError:
        print("exists.py [path-to-file-or-directory]")
        sys.exit(1)

    # Help argument
    if str(args[1]) == "-h":
        print("exists.py [path-to-file-or-directory]")
        sys.exit(1)
    
    # Checks if file exists (LOL)
    counter = 0
    for arg in args:
        if "exists.py" in arg and counter is 0:
            pass
        else:
            if not os.path.exists(arg):
                print("{} doesn't exist!".format(arg))
            else:
                print("{} exists!".format(arg))
        counter += 1
       
if __name__ == "__main__":
    main()