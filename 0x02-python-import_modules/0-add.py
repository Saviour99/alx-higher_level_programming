#!/usr/bin/python3

if __name__ == "__main__":
    # Import the add_0 module
    import add_0

    # Assign values to a and b
    a = 1
    b = 2

    # Perform addition and store the result
    result = add_0.add(a, b)

    # Print the formatted string
    print("{:d} + {:d} = {:d}".format(a, b, result))
