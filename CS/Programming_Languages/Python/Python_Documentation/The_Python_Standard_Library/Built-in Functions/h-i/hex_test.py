"""hex(x)"""
# https://www.programiz.com/python-programming/methods/built-in/hex

"""Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.
If x is not a python int object, it has to define an __index__() method that returns an integer."""
print(f"hex(255): {hex(255)}")
print(f"hex(-42): {hex(-42)}")
print(f'{255:#x}', f'{255:#X}', f'{255:x}', f'{255:X}\n')

number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

returnType = type(hex(number))
print(f'Return type from hex() is {returnType}\n')


"""If you need to find hexadecimal representation of a float, you need to use float.hex() method."""
number = 2.5
print(number, 'in hex =', float.hex(number))

number = 0.0
print(number, 'in hex =', float.hex(number))

number = 10.5
print(number, 'in hex =', float.hex(number))
