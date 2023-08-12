#!/usr/bin/python3

 import sys

    total = 0
    for a in range(len(sys.argv) - 1):
        total += int(sys.argv[a + 1])
    print("{}".format(total))
