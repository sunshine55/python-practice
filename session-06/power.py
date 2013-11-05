import types

def isPowerOfTwo(x):
    if type(x) is types.IntType:
        return (x & (x-1)) == 0
    return False