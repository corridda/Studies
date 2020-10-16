"""delattr(object, name)"""
# https://www.programiz.com/python-programming/methods/built-in/delattr

"""This is a relative of setattr(). The arguments are an object and a string.
The string must be the name of one of the object’s attributes.
The function deletes the named attribute, provided the object allows it.
For example, delattr(x, 'foobar') is equivalent to del x.foobar."""


class X:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def __repr__(self):
        return f"foo: {self.foo}\nbar: {self.bar}"


class Coordinate:
    x = 10
    y = -5
    z = 0


def main():
    x = X(1, 2)
    print(f"x:\n{x}\n")

    delattr(x, 'bar')
    try:
        print(x)
    except AttributeError as e:
        print(repr(e) + '\n')

    # another example
    point = Coordinate()

    print('x = ', point.x)
    print('y = ', point.y)
    print('z = ', point.z)

    delattr(Coordinate, 'z')
    # or like this
    del Coordinate.x

    print('--After deleting z attribute--')
    print('y = ', point.y)

    # Raises Error
    try:
        print('x = ', point.x)
    except AttributeError as e:
        print(repr(e))
    try:
        print('z = ', point.z)
    except AttributeError as e:
        print(repr(e))


if __name__ == "__main__":
    main()
