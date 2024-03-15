def magic_calculation(a, b):
    result = 98                # LOAD_CONST 1 (98)
    result += (a ** b)        # LOAD_FAST a, LOAD_FAST b, BINARY_POWER, BINARY_ADD
    return result              # RETURN_VALUE
