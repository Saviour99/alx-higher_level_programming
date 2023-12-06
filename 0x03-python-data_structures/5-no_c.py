#!/usr/bin/python3

def no_c(my_string):
    string = ""
    for c in my_string:
        if c == "c" or c == "C":
            continue
        string += c
    return string
