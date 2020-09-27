"""Bytes Objects"""

single_quotes = b'still allows embedded "double" quotes'
double_quotes = b"still allows embedded 'single' quotes"
triple_quotes = b'''3 single quotes''', b"""3 double quotes"""

print(f"single_quotes: {single_quotes}")
print(f"double_quotes: {double_quotes}")
print(f"triple_quotes: {triple_quotes}\n")


"""classmethod fromhex(string)
    This bytes class method returns a bytes object, decoding the given string object.
    The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.
"""
print(f"bytes.fromhex('2Ef0 F1f2  '): {bytes.fromhex('2Ef0 F1f2  ')}\n")


"""hex()
    Return a string object containing two hexadecimal digits for each byte in the instance.
"""
str_1 = b'\xf0\xf1\xf2'
print(f"str_1.hex(): {str_1.hex()}\n")


# You can always convert a bytes object into a list of integers using list(b).
print(f"list(str_1): {list(str_1)}\n")
