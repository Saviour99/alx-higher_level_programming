#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
            print(c, end="")
        else:
            s = chr(ord(c) - 32)
            print(s, end="")
    print()
