#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as av

    length = len(av)
    add = 0

    if length == 1:
        print("{:d}".format(length - 1))
    else:
        for i in range(1, length):
            add += int(av[i])
        print("{:d}".format(add))
