#!/usr/bin/python3

if __name__ == "__main__":
    """Print the result of various operations on 10 and 5."""
    from calculator_1 import add, sub, mul, div

    # Define variables a and b
    a = 10
    b = 5

    # Perform calculations and print results using a single print statement
    print("{} + {} = {}".format(a, b, add(a, b)),
          "{} - {} = {}".format(a, b, sub(a, b)),
          "{} * {} = {}".format(a, b, mul(a, b)),
          "{} / {} = {}".format(a, b, div(a, b)), sep="\n")
