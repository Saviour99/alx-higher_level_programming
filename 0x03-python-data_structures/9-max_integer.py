#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if my_list:
                if my_list[i] > my_list[i + 1]:
                    return my_list[i]
                else:
                    return my_list[i + 1]
