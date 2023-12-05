#!/usr/bin/python3

def element_at(my_list, idx):
    for x in my_list:
        if x == my_list[idx]:
            return x
    return None
