#!/usr/bin/python3

# iterating through the chars
for i in range(97, 123):
    if (i == 101) or (i == 113):
        continue
    print("{:c}".format(i), end="")
