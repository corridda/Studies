""" class str(object='')
    class str(object=b'', encoding='utf-8', errors='strict')"""
# https://www.programiz.com/python-programming/methods/built-in/str

"""Return a string version of object. If object is not provided, returns the empty string.
Otherwise, the behavior of str() depends on whether encoding or errors is given, as follows.

If neither encoding nor errors is given, str(object) returns object.__str__(), which is the “informal”
or nicely printable string representation of object. For string objects, this is the string itself.
If object does not have a __str__() method, then str() falls back to returning repr(object).

If at least one of encoding or errors is given, object should be a bytes-like object (e.g. bytes or bytearray).
In this case, if object is a bytes (or bytearray) object, then str(bytes, encoding, errors) is equivalent
to bytes.decode(encoding, errors). Otherwise, the bytes object underlying the buffer object
is obtained before calling bytes.decode(). See Binary Sequence Types — bytes, bytearray,
memoryview and Buffer Protocol for information on buffer objects.

Passing a bytes object to str() without the encoding or errors arguments falls
under the first case of returning the informal string representation (see also the -b command-line option to Python).
For example:
    >>> str(b'Zoot!')
    "b'Zoot!'"
"""


# Example 1: How str() works in Python?

"""If encoding and errors parameter isn't provided, str() method internally calls __str__() method of an object.
If it cannot find the __str__() method, it instead calls repr(obj)."""
print(f"str('10'): {str('10')}\n")



# Example 2: How str() works for bytes?

"""If encoding and errors parameter is provided, the first parameter (object) should be a bytes-like-object
(bytes or bytearray).
If the object is bytes or bytearray, str() method internally calls bytes.decode(encoding, errors).
Otherwise, it gets the bytes object in the buffer before calling the decode() method."""

# bytes
b = bytes('pythön', encoding='utf-8')
print(str(b, encoding='ascii', errors='ignore'))

"""Since, the character 'ö' cannot be decoded by ASCII, it gives out an error.
But, since we set the errors='ignore', it ignores the character which cannot be decoded by str(), i.e. ö
This results in the output 'pythn'."""
