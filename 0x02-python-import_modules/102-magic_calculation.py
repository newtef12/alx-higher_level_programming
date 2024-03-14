#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Replicates the behavior of the given bytecode.
    """
    import magic_calculation_102

    # Import add and sub functions from magic_calculation_102
    add = magic_calculation_102.add
    sub = magic_calculation_102.sub

    # Check if a is less than b
    if a < b:
        # Calculate c as the result of adding a and b
        c = add(a, b)
        # Add numbers from 4 to 5 to c
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        # Return the result of subtracting b from a
        return sub(a, b)
