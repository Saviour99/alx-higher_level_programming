#!/usr/bin/python3

if __name__ == "__main__":
    # Import the add_0 module
    from add_0 import add

    # Assign values to a and b
    a = 1
    b = 2

    # Print the formatted string
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
