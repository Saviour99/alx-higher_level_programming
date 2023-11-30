#!/usr/bin/python3

if __name__ == "__main__":
    import sys
'''
    n = sys.argv
    l = len(n)

    for i in range(0, int(l)): 
        if sys.argv[i] == sys.argv[0]:
            print("{} {}.".format(i, "arguments"))
            continue
        elif sys.argv[i] == sys.argv[1]:
            print("{} {}".format(i, "argument:"))
            print("{}: {}".format(i, sys.argv[1]))
'''

    num = sys.argv[:-1]
    length = len(num)

    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:")
    else:
        print(f"{length} arguments:")

    for i in range(1, length):
        print(f"{i}: {sys.argv[i]}")

