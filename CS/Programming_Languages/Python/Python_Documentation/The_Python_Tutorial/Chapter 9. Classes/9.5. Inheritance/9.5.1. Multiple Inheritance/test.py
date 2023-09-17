# python supports a form of multiple inheritance as well

class A():
    in_A = 'A'

    def __init__(self, a):
        self.a = a

    def print_message(self):
        print("It's in A.")


class B():
    in_B = 'B'

    def __init__(self, b):
        self.b = b

    def print_message(self):
        print("It's in B.")


# 'C' is a subclass of 'A' and 'B' at the same time
class C(A, B):
    def __init__(self, a, b, c):
        A.a = a
        B.b = b
        self.c = c

    # overridden method
    def print_message(self):
        print("It's in C.")
        B.print_message(self)
        A.print_message(self)


c_obj = C(1, 2, 3)
print('c_obj.a:', c_obj.a)
print('c_obj.b:', c_obj.b)
print('c_obj.c:', c_obj.c)
print('c_obj.in_A:', c_obj.in_A)
print('c_obj.in_B:', c_obj.in_B)
print('\nisinstance(c_obj, (A, B)):', isinstance(c_obj, (A, B)))
print('issubclass(C, (A, B)):', issubclass(C, (A, B)))
print()
c_obj.print_message()
