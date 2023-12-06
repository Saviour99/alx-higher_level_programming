#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        first_char = sentence[0]
        result = (length, first_char)
        return result
    else:
        first_char = None
        result = (length, first_char)
        return result
