#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as av
    from calculator_1 import add, sub, mul, div

    ac = len(av)
    a = int(av[1])
    b = int(av[3])

    if ac != 4:
        print("Usage: {} <a> <operator> <b>".format(av[0]))
        exit(1)

    if av[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif av[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif av[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif av[2] == "/":
        if b == 0:
            print("Division by zero is not allowed")
            exit(1)
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
