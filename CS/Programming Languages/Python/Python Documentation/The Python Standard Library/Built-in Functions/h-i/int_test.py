"""class int(x=0), class int(x, base=10)"""
# https://www.programiz.com/python-programming/methods/built-in/int

"""Return an integer object constructed from a number or string x, or return 0 if no arguments are given.
If x defines __int__(), int(x) returns x.__int__(). If x defines __trunc__(), it returns x.__trunc__().
For floating point numbers, this truncates towards zero."""


class I:
    def __init__(self, a):
        self.__a = a
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, new_a):
        self.__a = new_a
    def __int__(self):
        return self.__a


class T:
    def __init__(self, b):
        self.b = b
    def __trunc__(self):
        from math import trunc
        return trunc(self.b)

if __name__ == '__main__':
    print(f"int(): {int()}\n")

    i_obj = I(10)
    print(f"i_obj.a: {i_obj.a}")
    i_obj.a = 20
    print(f"i_obj: {i_obj}")
    print(f"i_obj.a: {i_obj.a}")
    print(f"int(i_obj): {int(i_obj)}\n")

    t_obj = T(15.9)
    print(f"t_obj.b: {t_obj.b}")
    print(f"int(t_obj): {int(t_obj)}\n")

    # binary 0b or 0B
    print(f"int('1010', base=2): {int('1010', base=2)}")
    print(f"int('0b1010', base=2): {int('0b1010', base=2)}")

    # octal 0o or 0O
    print(f"int('12', 8): {int('12', 8)}")
    print(f"int('0o12', 8): {int('0o12', 8)}")

    # hexadecimal
    print(f"int('A', 16): {int('A', 16)}")
    print(f"int('0xA', 16): {int('0xA', 16)}\n")