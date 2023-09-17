"""oct(x)"""
# https://www.programiz.com/python-programming/methods/built-in/oct

"""Convert an integer number to an octal string prefixed with “0o”. The result is a valid python expression.
If x is not a python int object, it has to define an __index__() method that returns an integer."""

# Example 1: How oct() works in python?
# decimal number
print('oct(10) is:', oct(10))

# binary number
print('oct(0b101) is:', oct(0b101))

# hexadecimal number
print('oct(0XA) is:', oct(0XA))


# Example 2: How oct() for custom objects by implementing __index__()?
class Person:
    """Note: For previous compatibility, implement __int__() and __index__() with the same output."""
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print(f'The oct is: {oct(person)}\n')


"""If you want to convert an integer number to octal string either with prefix “0o” or not,
you can use either of the following ways."""

print('%#o' % 10, '%o' % 10)
print(format(10, '#o'), format(10, 'o'))
print(f'{10:#o}', f'{10:o}')