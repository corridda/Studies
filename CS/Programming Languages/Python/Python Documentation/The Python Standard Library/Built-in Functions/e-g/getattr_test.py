"""getattr(object, name[, default])"""
# https://www.programiz.com/python-programming/methods/built-in/getattr

"""Return the value of the named attribute of object. 'name' must be a string.
The above syntax is equivalent to: 'object.name'."""


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


obj_1 = A(1, 2)
obj_2 = 15
print(f"getattr(obj_1, 'a'): {getattr(obj_1, 'a')}")
print(f"getattr(obj_1, 'b'): {getattr(obj_1, 'b')}")

# If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.
print(f"getattr(obj_2, 'a', None): {getattr(obj_2, 'a',  None)}\n")
try:
    print(f"getattr(obj_2, 'b'): {getattr(obj_2, 'b')}")
except AttributeError as e:
    print(repr(e))
    print()


# Examples
class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age, '\n')

