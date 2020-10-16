"""Bytearray Objects"""

"""classmethod fromhex(string)
    This bytearray class method returns bytearray object, decoding the given string object.
    The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.
"""
print(f"bytearray.fromhex('2Ef0 F1f2  '): {bytearray.fromhex('2Ef0 F1f2  ')}\n")



"""hex()
    Return a string object containing two hexadecimal digits for each byte in the instance.
"""
b_arr = bytearray(b'.\xf0\xf1\xf2')
print(f"b_arr.hex(): {b_arr.hex()}\n")


# You can always convert a bytearray object into a list of integers using list(b).
print(f"list(b_arr): {list(b_arr)}")
