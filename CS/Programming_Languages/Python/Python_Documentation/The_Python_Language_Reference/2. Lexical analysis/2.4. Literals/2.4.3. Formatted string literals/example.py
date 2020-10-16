import decimal
from datetime import datetime

a = 1
b = 10.5
print(f"{{a}} = {a}")
print(f"b = {b:.2f}")

name = "Fred"
print(f"He said his name is {name!r}.")
print(f"He said his name is {repr(name)}.")  # repr() is equivalent to !r

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")  # nested fields

today = datetime(year=2018, month=6, day=10)
print(f"{today:%B %d, %Y}")  # using date format specifier

number = 1024
print(f"{number:#0x}")  # using integer format specifier

# Backslashes are not allowed in format expressions
# raises SyntaxError
# print(f"newline: {ord('\n')}")

# To include a value in which a backslash escape is required, create a temporary variable.
temp = ord('\n')
print(f"newline: {temp}")

