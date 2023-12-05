#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for i in my_list:
        j = i + 1
        if j == idx:

            return element
            break
    else:
        return my_list
