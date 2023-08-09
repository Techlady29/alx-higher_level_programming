#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 101:
        continue
    elif letter == 113:
        continue
    print("{}".format(chr(letter)), end="")
