"""Additional Methods on Integer Types"""

"""int.bit_length()
    Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:
"""
n = -37
print(bin(n))
print(f"n.bit_length(): {n.bit_length()}\n")


"""int.to_bytes(length, byteorder, *, signed=False)
    Return an array of bytes representing an integer.
"""
print((1024).to_bytes(2, byteorder='big'))
print((1024).to_bytes(10, byteorder='big'))
print((-1024).to_bytes(10, byteorder='big', signed=True))
x = 1000
print(x.to_bytes((x.bit_length() + 7) // 8, byteorder='little'),  '\n')


"""classmethod int.from_bytes(bytes, byteorder, *, signed=False)
    Return the integer represented by the given array of bytes.
"""
print(int.from_bytes(b'\x00\x10', byteorder='big'))
print(int.from_bytes(b'\x00\x10', byteorder='little'))