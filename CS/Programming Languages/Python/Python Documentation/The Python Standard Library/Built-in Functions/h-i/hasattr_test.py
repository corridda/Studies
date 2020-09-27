"""hasattr(object, name)"""
# https://www.programiz.com/python-programming/methods/built-in/hasattr


print(f"'int' has 'real': {hasattr(int, 'real')}\n")


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


obj_1 = A(1, 2)
obj_2 = 15
print(f"hasattr(obj_1, 'a'): {hasattr(obj_1, 'a')}")
print(f"hasattr(obj_1, 'b'): {hasattr(obj_1, 'b')}")
print(f"getattr(obj_2, 'a'): {hasattr(obj_2, 'a')}\n")


class Person:
    age = 23
    name = 'Adam'


person = Person()
print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))
