#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add

    # Define variables a and b
    a = 1
    b = 2

    # Print the addition result using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))
