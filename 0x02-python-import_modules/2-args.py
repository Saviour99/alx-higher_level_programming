#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv[1:])

    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:")
    else:
        print(f"{length} arguments:")

    for i in range(1, length + 1):
        print(f"{i}: {argv[i]}")

