"""bin(x)"""
# https://www.programiz.com/python-programming/methods/built-in/bin

"""Convert an integer number to a binary string prefixed with “0b”.
The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method
that returns an integer. Some examples:"""


class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


def main():
    print(f"bin(3): {bin(3)}")
    print(f"bin(-10): {bin(-10)}\n")

    """If prefix “0b” is desired or not, you can use either of the following ways."""
    a = format(14, '#b'), format(14, 'b')
    b = f'{14:#b}', f'{14:b}'
    print(a)
    print(b)

    number = 5
    print('\nThe binary equivalent of 5 is:', bin(number))

    # Convert an object to binary implementing __index__() method
    print('The binary equivalent of quantity is:', bin(Quantity()))


if __name__ == "__main__":
    main()
