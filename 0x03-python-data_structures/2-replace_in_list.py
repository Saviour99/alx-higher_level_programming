#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for i in my_list:
        if i == my_list[idx]:
            i = element
            return my_list
    else:
        return my_list
