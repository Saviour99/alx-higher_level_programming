#usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    result = 0

    for elm in uniq:
        result += elm
    return result
