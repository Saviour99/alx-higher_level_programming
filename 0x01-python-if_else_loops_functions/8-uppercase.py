#!/usr/bin/python3
def uppercase(str):
    for character in str:
        char = character
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(character) - 32)
        print("{}".format(char), end="")
    print()
