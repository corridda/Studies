"""https://t.me/pythonetc/237"""

"""The problem with calling repr of other objects in your own __repr__ method is that you can't guarantee
none of the other objects is not equal to self and the call isn't recursive:"""

import reprlib


class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.left!r}, {self.right!r})'


if __name__ == '__main__':
    p = Pair(1, 2)
    print(p)
    p.right = p
    try:
        print(p)
    except RecursionError as e:
        print(repr(e))


    # To easily solve this problem you can use reprlib.recursive_repr decorator
    class Pair_2:
        def __init__(self, left, right):
            self.left = left
            self.right = right

        @reprlib.recursive_repr()
        def __repr__(self):
            class_name = type(self).__name__
            return f'{class_name}({self.left!r}, {self.right!r})'


    # Now it works:
    p = Pair_2(1, 2)
    p.right = p
    print(p)
