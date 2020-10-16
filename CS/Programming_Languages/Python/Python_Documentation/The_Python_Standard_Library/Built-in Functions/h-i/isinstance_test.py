"""isinstance(object, classinfo)"""
# https://www.programiz.com/python-programming/methods/built-in/isinstance

"""Return true if the object argument is an instance of the classinfo argument,
or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type,
the function always returns false. If classinfo is a tuple of type objects (or recursively, other such tuples),
return true if object is an instance of any of the types. If classinfo is not a type or tuple of types
and such tuples, a TypeError exception is raised."""


class Foo:
    a = 5

class Bar(Foo):
    bar = 10


# Example 1: How isinstance() works?
fooInstance = Foo()
barInstance = Bar()
print(f"isinstance(fooInstance, Foo): {isinstance(fooInstance, Foo)}")
print(f"isinstance(fooInstance, (list, tuple)): {isinstance(fooInstance, (list, tuple))}")
print(f"isinstance(fooInstance, (list, tuple, Foo)): {isinstance(fooInstance, (list, tuple, Foo))}")
print(f"isinstance(barInstance, Bar): {isinstance(barInstance, Bar)}")
print(f"isinstance(barInstance, Foo): {isinstance(barInstance, Foo)}")
print(f"isinstance(fooInstance, Bar): {isinstance(fooInstance, Bar)}\n")


# Example 2: Working of isinstance() with Native Types
numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers,'instance of list?', result)

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)

result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result)

number = 5

result = isinstance(number, list)
print(number,'instance of list?', result)

result = isinstance(number, int)
print(number,'instance of int?', result)