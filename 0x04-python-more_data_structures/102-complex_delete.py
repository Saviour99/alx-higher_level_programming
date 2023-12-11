#!/usr/bin/python3

def complex_delete(my_dict, value):
    res = {}
    if not value:
        return my_dict
    for key, val in my_dict.items():
        if val != value:
            res[key] = val
    my_dict.clear()
    my_dict.update(res)
    return my_dict
