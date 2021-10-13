#!/usr/bin/python3

import sys


from pathlib import Path

def find_by_group(path, group):
    for i in path.glob("**/*"):
        if i.group() == group:
            yield i
    
def copyTo():
    pass




def main():
    user_group = sys.argv[1:]
    #could be better with argparse lib
    pass

if __name__ == "__main__":
    main()