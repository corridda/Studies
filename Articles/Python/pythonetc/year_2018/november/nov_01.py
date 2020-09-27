"""https://t.me/pythonetc/236"""

"""
When you write custom __repr__ for some object, you usually want to include representation of its attributes.
For that, you should make formatting call repr() on objects, since it calls str() by default.
It is done with the !r notation:
"""

class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.left!r}, {self.right!r})'

if __name__ == '__main__':
    pair = Pair('left', 'right')
    print(f"pair: {pair}")