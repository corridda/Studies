"""Bytes and Bytearray Operations"""

"""The following methods on bytes and bytearray objects can be used with arbitrary binary data.
    bytes.count(sub[, start[, end]])
    bytearray.count(sub[, start[, end]])
"""
single_quotes = b'still allows embedded "double" quotes'
print(f"single_quotes.count(b's'): {single_quotes.count(b's')}")
b_arr = bytearray(b'.\xf0\xf1\xf2\xf1\xf3\xf1')
print(f"b_arr.count(241): {b_arr.count(241)}\n")


"""bytes.decode(encoding="utf-8", errors="strict")
bytearray.decode(encoding="utf-8", errors="strict")"""
b_arr_2 = bytearray(b'\x58\x59\x5A')
print(f"b_arr_2: {b_arr_2}")
print(f"b_arr_2.decode(errors='ignore'): {b_arr_2.decode(errors='ignore')}\n")


"""bytes.endswith(suffix[, start[, end]])
bytearray.endswith(suffix[, start[, end]])"""
print(f"b_arr_2.endswith((b'Z', b'A')): {b_arr_2.endswith((b'Z', b'A'))}\n")


"""bytes.find(sub[, start[, end]])
bytearray.find(sub[, start[, end]])"""
print(f"bytearray(b'def-abcdef-abcdef-abc-abc-def').find(b'abc'): "
      f"{bytearray(b'def-abcdef-abcdef-abc-abc-def').find(b'abc')}\n")
"""Note: The find() method should be used only if you need to know the position of sub.
To check if sub is a substring or not, use the in operator:"""
print(f"b'Py' in b'Python': {b'Py' in b'Python'}\n")


"""bytes.index(sub[, start[, end]])
bytearray.index(sub[, start[, end]])"""
try:
    print(f"{bytearray(b'def-abcdef-abcdef-abc-abc-def').index(b'eee')}")
except ValueError as e:
    print(repr(e))
print()



"""bytes.partition(sep)
bytearray.partition(sep)"""
print(f"single_quotes: {single_quotes}")
print(f"single_quotes.partition(b' '): {single_quotes.partition(b' ')}")
print(f"single_quotes.partition(b'eee'): {single_quotes.partition(b'eee')}\n")



"""bytes.replace(old, new[, count])
bytearray.replace(old, new[, count])"""
print(f"bytearray(b'def-abcdef-abcdef-abc-abc-def').replace(b'abc', b'aaa'): "
      f"{bytearray(b'def-abcdef-abcdef-abc-abc-def').replace(b'abc', b'aaa')}\n")



"""bytes.rfind(sub[, start[, end]])
bytearray.rfind(sub[, start[, end]])"""
print(f"b'def-abcdef-abcdef-abc-abc-def'.rfind(b'abc'): "
      f"{b'def-abcdef-abcdef-abc-abc-def'.rfind(b'abc')}\n")


"""bytes.rindex(sub[, start[, end]])
bytearray.rindex(sub[, start[, end]])"""
try:
    print(f"b'def-abcdef-abcdef-abc-abc-def'.rindex(b'eee'): "
          f"{b'def-abcdef-abcdef-abc-abc-def'.rindex(b'eee')}\n")
except ValueError as e:
    print(repr(e))
print()


"""bytes.rpartition(sep)
bytearray.rpartition(sep)"""
print(f"single_quotes: {single_quotes}")
print(f"single_quotes.rpartition(b' '): {single_quotes.rpartition(b' ')}")
print(f"single_quotes.rpartition(b'eee'): {single_quotes.rpartition(b'eee')}\n")


"""bytes.startswith(prefix[, start[, end]])
bytearray.startswith(prefix[, start[, end]])"""
print(f"b'def-abcdef-abcdef-abc-abc-def'.startswith(b'def'): "
      f"{b'def-abcdef-abcdef-abc-abc-def'.startswith(b'def')}\n")


"""bytes.translate(table, delete=b'')
bytearray.translate(table, delete=b'')"""
print(f"b'read this short text'.translate(None, b'aeiou'): "
      f"{b'read this short text'.translate(None, b'aeiou')}\n")


"""bytes.center(width[, fillbyte])
bytearray.center(width[, fillbyte])"""
print(f"single_quotes.center(50, b'*'):\n{single_quotes.center(50, b'*')}\n")


"""bytes.ljust(width[, fillbyte])
bytearray.ljust(width[, fillbyte])"""
print(f"single_quotes.ljust(50, b'*'):\n{single_quotes.ljust(50, b'*')}\n")


"""bytes.lstrip([chars])
bytearray.lstrip([chars])
The chars argument is not a prefix; rather, all combinations of its values are stripped:"""
phrase_ws = b' \t some binary string... \t \t '
print(f"phrase_ws.lstrip(): {phrase_ws.lstrip()}")
print(f"b'www.example.com'.lstrip(b'cmowz.'): {b'www.example.com'.lstrip(b'cmowz.')}\n")


"""bytes.rjust(width[, fillbyte])
bytearray.rjust(width[, fillbyte])"""
print(f"single_quotes.rjust(50, b'*'):\n{single_quotes.rjust(50, b'*')}\n")


"""bytes.rsplit(sep=None, maxsplit=-1)
bytearray.rsplit(sep=None, maxsplit=-1)"""
print(f"single_quotes.rsplit(maxsplit=2): {single_quotes.rsplit(maxsplit=2)}\n")


"""bytes.rstrip([chars])
bytearray.rstrip([chars])"""
phrase_ws = b' \t some binary string... \t \t '
print(f"phrase_ws.rstrip(): {phrase_ws.rstrip()}")
print(f"b'mississippi'.rstrip(b'ipz'): {b'mississippi'.rstrip(b'ipz')}\n")


"""bytes.split(sep=None, maxsplit=-1)
bytearray.split(sep=None, maxsplit=-1)"""
print(f"single_quotes.split(maxsplit=2): {single_quotes.split(maxsplit=2)}")
print(f"single_quotes.split(b'allows): {single_quotes.split(b'allows')}\n")


"""bytes.strip([chars])
bytearray.strip([chars])"""
print(f"phrase_ws.strip(): {phrase_ws.strip()}")
print(f"b'www.example.com'.strip(b'cmowz.'): {b'www.example.com'.strip(b'cmowz.')}\n")


"""bytes.capitalize()
bytearray.capitalize()"""
print(f"phrase_ws.strip().capitalize(): {phrase_ws.strip().capitalize()}\n")


"""bytes.expandtabs(tabsize=8)
bytearray.expandtabs(tabsize=8)"""
bytes_1 = b'unit_01\t012\t0123\t01234'
print(f"bytes_1.expandtabs():\n{bytes_1.expandtabs()}")
print(f"bytes_1.expandtabs(tabsize=4):\n{bytes_1.expandtabs(tabsize=4)}\n")


"""bytes.isalnum()
bytearray.isalnum()"""
print(f"bytes.isalnum(b'ab12'): {bytes.isalnum(b'ab12')}")
print(f"bytes.isalnum(b'**ab12**'): {bytes.isalnum(b'**ab12**')}\n")


"""bytes.isalpha()
bytearray.isalpha()"""
print(f"b'ABCabc'.isalpha(): {b'ABCabc'.isalpha()}")
print(f"b'ABCabc1'.isalpha(): {b'ABCabc1'.isalpha()}\n")


"""bytes.isascii()
bytearray.isascii()"""
print(f"b''.isascii(): {b''.isascii()}")
bytes_2 = b'\x16.\x58\x59\x5A'
print(f"bytes_2: {bytes_2}")
print(f"bytes_2.isascii(): {bytes_2.isascii()}\n")


"""bytes.isdigit()
bytearray.isdigit()"""
print(f"b'1234'.isdigit(): {b'1234'.isdigit()}")
print(f"b'1.23'.isdigit(): {b'1.23'.isdigit()}\n")


"""bytes.islower()
bytearray.islower()"""
print(f"b'hello world'.islower(): {b'hello world'.islower()}")
print(f"b'Hello world'.islower(): {b'Hello world'.islower()}\n")


"""bytes.isspace()
bytearray.isspace()"""
bytes_3 = b' \t\n\r\x0b\f'
print(f"b''.isspace(): {b''.isspace()}")
print(f"bytes_3.isspace(): {bytes_3.isspace()}\n")


"""bytes.istitle()
bytearray.istitle()"""
print(f"b'Hello World'.istitle(): {b'Hello World'.istitle()}")
print(f"b'Hello world'.istitle(): {b'Hello world'.istitle()}\n")


"""bytes.isupper()
bytearray.isupper()"""
print(f"b'HELLO WORLD'.isupper(): {b'HELLO WORLD'.isupper()}")
print(f"b'Hello world'.isupper(): {b'Hello world'.isupper()}\n")


"""bytes.lower()
bytearray.lower()"""
print(f"b'Hello World'.lower(): {b'Hello World'.lower()}\n")


"""bytes.splitlines(keepends=False)
bytearray.splitlines(keepends=False)"""
bytes_4 = b'ab c\n\nde fg\rkl\r\n'
print(f"bytes_4.splitlines(): {bytes_4.splitlines()}")
print(f"bytes_4.splitlines(keepends=True): {bytes_4.splitlines(keepends=True)}\n")


"""bytes.swapcase()
bytearray.swapcase()"""
print(f"b'Hello World'.swapcase(): {b'Hello World'.swapcase()}\n")


"""bytes.title()
bytearray.title()"""
print(f"b'Hello world'.title(): {b'Hello world'.title()}\n")


"""bytes.upper()
bytearray.upper()"""
print(f"b'Hello World'.upper(): {b'Hello World'.upper()}\n")


"""bytes.zfill(width)
bytearray.zfill(width)"""
print(f"b'42'.zfill(5): {b'42'.zfill(5)}")
print(f"b'-42'.zfill(5): {b'-42'.zfill(5)}\n")
