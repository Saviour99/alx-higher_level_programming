#!/usr/bin/python3

def element_at(my_list, idx):
    for x in my_list:
        if x == idx:
            return x + 1
    return None
