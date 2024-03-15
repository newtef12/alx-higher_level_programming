def magic_calculation(a, b):
    result = 0                 # LOAD_CONST 0 (0)
    result += 98               # LOAD_CONST 1 (98), BINARY_ADD
    result += (a ** b)         # LOAD_FAST a, LOAD_FAST b, BINARY_POWER, BINARY_ADD
    return result              # RETURN_VALUE
