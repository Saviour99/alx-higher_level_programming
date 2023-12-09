#!/usr/bin/python3

def common_elements(set_1, set_2):
        for elm in set_1:
            if elm in set_2:
                result = list(elm)
            return result
