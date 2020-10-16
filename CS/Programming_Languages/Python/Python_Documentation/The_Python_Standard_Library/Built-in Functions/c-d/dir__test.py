"""dir([object])"""
# https://www.programiz.com/python-programming/methods/built-in/dir

"""The dir() method tries to return a list of valid attributes of the object.
Without arguments, return the list of names in the current local scope.
With an argument, attempt to return a list of valid attributes for that object."""

import struct


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


def main():
    a = 1
    b = 'string'
    c = []
    print(f"dir(): {dir()}")
    print(f"dir(a): {dir(a)}\n")

    s = Shape()
    print(f"dir(): {dir()}")
    print(f"dir(s): {dir(s)}\n")
    print(f"dir() + dir(s): {dir() + dir(s)}")

    print(f"dir(struct):\n{dir(struct)}")


if __name__ == "__main__":
    main()
