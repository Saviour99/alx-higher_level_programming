#!/usr/bin/python3

def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char

        # Use the first print function to print each character without a new line
        print(uppercase_char, end='')

    # Use the second print function to print a new line after the entire string
    print()
