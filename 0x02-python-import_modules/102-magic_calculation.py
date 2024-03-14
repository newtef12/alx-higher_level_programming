#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    import magic_calculation_102

    if a < b:
        c = magic_calculation_102.add(a, b)
        for i in range(4, 6):
            c = magic_calculation_102.add(c, i)
        return c
    else:
        return magic_calculation_102.sub(a, b)
