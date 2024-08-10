#!/usr/bin/env python3

import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    search_string = sys.argv[2]

    match = re.findall(re.escape(keyword), search_string)
    if match:
        print(len(match))
    else:
        print("none.")

if __name__ == "__main__":
    main()