#!/usr/bin/python3
'''
def uppercase(str):
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
            print("{}".format(c), end="")
        else:
            s = chr(ord(c) - 32)
            print("{}".format(s), end="")
    print()
'''

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        print(uppercase_char, end='')

    print()
