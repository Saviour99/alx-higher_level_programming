#!/usr//bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if idx >= 0 and idx < lenght:
        return my_list[idx]
    else:
        return None
