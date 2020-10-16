"""format(value[, format_spec])"""
# https://www.programiz.com/python-programming/methods/built-in/format

"""Convert a value to a “formatted” representation, as controlled by format_spec."""

"""The format specifier could be in the format:

[[fill]align][sign][#][0][width][,][.precision][type]
where, the options are
fill        ::=  any character
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%" """

"""Number formatting with format()"""
# d, f and b are type

# integer
print(f"format(123, 'd'): {format(123, 'd')}")

# float arguments
print(f"format(123.4567898, 'f'): {format(123.4567898, 'f')}")

# binary format
print(f"format(12, 'b'): {format(12, 'b')}\n")




"""Number formatting with fill, align, sign, width, precision and type"""

# integer
print(f'format(1234, "*>+7,d"): {format(1234, "*>+7,d")}')

# float number
print(f'format(123.4567, "^-09.3f"): {format(123.4567, "^-09.3f")}\n')

"""
Here, when formatting the integer 1234, we've specified the formatting specifier *<+7,d. Let's get to each option:

* - It is the fill character that fills up the empty spaces after formatting
> - It is the right alignment option that aligns the output string to the right
+ - It is the sign option that forces the number to be signed (having a sign on its left)
7 - It is the width option that forces the number to take a minimum width of 7, other spaces
will be filled by fill character
, - It is the thousands operator that places a comma between all thousands.
d - It is the type option that specifies the number is an integer.
When formatting the floating point number 123.4567, we've specified the format specifier ^-09.3f. These are:

^ - It is the center alignment option that aligns the output string to the center of the remaining space
- - It is the sign option that forces only negative numbers to show the sign
0 - It is the character that is placed in place of the empty spaces.
9 - It is the width option that sets the minimum width of the number to 9 (including decimal point,
thousands comma and sign)
.3 - It is the precision operator that sets the precision of the given floating number to 3 places
f - It is the type option that specifies the number is a float.
"""


"""Using format() by overriding __format__()"""

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

# The format() method internally runs Person().__format__("age") to return 23.
print(format(Person(), "age"))