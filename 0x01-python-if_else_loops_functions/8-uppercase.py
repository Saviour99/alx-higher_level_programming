#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            result += chr(ord(c) - ord("a") + ord("A"))
        else:
            result += c
    print(result)
    print()
