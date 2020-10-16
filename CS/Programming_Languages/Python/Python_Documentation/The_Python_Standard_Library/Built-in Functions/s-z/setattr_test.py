"""setattr(object, name, value)"""
# https://www.programiz.com/python-programming/methods/built-in/setattr

"""This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value.
The string may name an existing attribute or a new attribute. The function assigns the value to the attribute,
provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123."""


# Example 1: How setattr() works in Python?

class Person:
    name = 'Adam'


p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'John')

print(f'After modification: {p.name}\n')



# Example 2: setattr() when named attribute is not found and setting attribute to None

"""If the attribute is not found, setattr() creates a new attribute by the given name and value.
However, this is only possible if the object implements __dict__() method.
You can check if it does by using dir() method."""


class Person:
    name = 'Adam'


p = Person()

# setting attribute name to None
setattr(p, 'name', None)
print('Name is:', p.name)

# setting an attribute not present in Person
if '__dict__' in dir(Person):
    setattr(p, 'age', 23)
    print('Age is:', p.age)
else:
    print("There's no __dict__ method in there.")
