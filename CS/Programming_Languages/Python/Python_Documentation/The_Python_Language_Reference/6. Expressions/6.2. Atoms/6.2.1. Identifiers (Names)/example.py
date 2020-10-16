# When an identifier that textually occurs in a class definition begins with two or more
# underscore characters and does not end in two or more underscores,
# it is considered a private name of that class.

class MyClass():
    def __init__(self, a: int, b: int):
        self.__a = a
        self.b = b


my_class = MyClass(10, 20)

try:
    print(f"my_class.a: {my_class.a}")
except AttributeError as e:
    print(repr(e))
print(f"my_class.b: {my_class.b}")
