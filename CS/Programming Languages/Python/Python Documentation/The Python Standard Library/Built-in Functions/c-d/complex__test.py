"""class complex([real[, imag]])"""
# https://www.programiz.com/python-programming/methods/built-in/complex

"""Return a complex number with the value real + imag*1j or convert a string or number to a complex number."""


def main():
    print(f"complex(): {complex()}")
    print(f"complex(1): {complex(1)}")
    print(f"complex(2, -3): {complex(2, -3)}")
    print(f"complex(1.2, -5.6): {complex(1.2, -5.6)}")
    print(f"complex('1+5j'): {complex('1+5j')}")
    try:
        print(f"complex('1 + 5j'): {complex('1 + 5j')}")
    except ValueError as e:
        print(repr(e) + '\n')

    # Create complex Number Without Using complex()
    a = 2 + 3j
    print('a =', a)
    print('Type of a is', type(a))

    b = -2j
    print('b =', b)
    print('Type of b is', type(a))

    c = 0j
    print('c =', c)
    print('Type of c is', type(c))


if __name__ == "__main__":
    main()
