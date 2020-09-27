"""hash(object)"""
# https://www.programiz.com/python-programming/methods/built-in/hash

from dataclasses import dataclass


print(f"hash(1): {hash(1)}")
print(f"hash(1.0): {hash(1.0)}")
print(f"hash(100): {hash(100)}")


# Обратите внимание, что значение хэша значения должно быть одинаковым для одного запуска Python.
print(f"hash(aa): {hash('aa')}")
print(f"hash(aaa): {hash('aaa')}\n")

# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:', hash(181.23))

# The hash() method only works for immutable objects as tuple.
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print('The hash is:', hash(vowels), '\n')


d = dict([('a', 1), ('b', 2)])
print(f"d: {d}")
print(f"'a' in d: {'a' in d}")
print(f"hash('a'): {hash('a')}")
print(f"hash('a') in d: {hash('a') in d}\n")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        print('This is a hash:')
        return hash((self.name, self.age))

person_1 = Person(25, 'Jane')
person_2 = Person(25, 'Jane')
print(f"person_1: {person_1}")
print(f"person_2: {person_2}")
print(f"person_1.__eq__(person_2): {person_1.__eq__(person_2)}")
print(f"person_1.__hash__(): {person_1.__hash__()}")
print(f"person_2.__hash__(): {person_2.__hash__()}\n")


@dataclass(order=True)
class Test:
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __hash__(self):
        return hash((self.a, self.b))

test_1 = Test(1, 2)
test_2 = Test(1, 2)
print(f"test_1.__eq__(test_2: {test_1.__eq__(test_2)}")
print(f"test_1.__hash__(): {test_1.__hash__()}")
print(f"test_2.__hash__(): {test_2.__hash__()}\n")

