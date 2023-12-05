#!/usr/bin/python3

def element_at(my_list, idx):
    for x in my_list:
        if x == my_list[idx]:
            return my_list[idx]
    else:
        return None
