"""Инстанцирование"""

"""__init__ не будет вызван, если __new__ возвращает объект, не являющийся экземпляром исходного класса.
В этом случае объект мог быть создан другим классом, и значит __init__ уже вызывался на объекте:"""

class Foo:
    def __new__(cls, x):
        return dict(x=x)

    def __init__(self, x):
        print(x)  # Never called


print(Foo(0))



"""Это также означает, что не следует создавать экземпляры того же класса в __new__
с помощью обычного конструктора (Foo(...)). Это может привести к повторному исполнению __init__,
или даже к бесконечной рекурсии."""

# Бесконечная рекурсия:
class Foo:
    def __new__(cls, x):
        return Foo(-x)  # Recursion

try:
    print(Foo(0))
except RecursionError as e:
    print(repr(e) + '\n')


# Двойное исполнение __init__:
class Foo:
    def __new__(cls, x):
        if x < 0:
            return Foo(-x)
        return super().__new__(cls)

    def __init__(self, x):
        print(x)
        self._x = x

print(Foo(-100), '\n')


# Правильный способ:
class Foo:
    def __new__(cls, x):
        if x < 0:
            return cls.__new__(cls, -x)
        return super().__new__(cls)

    def __init__(self, x):
        print(x)
        self._x = x

print(Foo(-100))



