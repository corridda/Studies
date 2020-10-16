class A():
    in_A = 100

    def __init__(self, a):
        self.a = a

    def print_message(self):
        print("It's in A.")
        # # a method of a derived class may be called out of here
        # B.print_message(self)
        # C.print_message(self)


class B(A):
    def __init__(self, a, b):
        A.a = a
        self.b = b

    # overridden method
    def print_message(self):
        print("It's in B.")
        # a method of a base class may be called out of here
        A.print_message(self)


class C(B):
    def __init__(self, a, b, c):
        A.a = a
        B.b = b
        self.c = c

    # overridden method
    def print_message(self):
        print("It's in C.")



a_obj = A(0)
print(type(a_obj))

# check if the 'a_obj' is an instance of 'A'
print('isinstance(a_obj, A):', isinstance(a_obj, A))
print('isinstance(a_obj, B):', isinstance(a_obj, B))
print('isinstance(a_obj, C:', isinstance(a_obj, C))

# access to print_message()
a_obj.print_message()
A.print_message(self=a_obj)
print()



b_obj = B(1, 2)
print(type(b_obj))

# check if the 'b_obj' is an instance of 'A' or an instance of 'B'
print('isinstance(b_obj, (A, B)):', isinstance(b_obj, (A, B)))
print('isinstance(b_obj, A):', isinstance(b_obj, A))

# check if the 'B' - class is a subclass of 'A'
print('issubclass(B, A):', issubclass(B, A))
print('issubclass(B, C):', issubclass(B, C))

print('b_obj.a:', b_obj.a)
print('b_obj.b:', b_obj.b)
print('b_obj.in_A:', b_obj.in_A)
b_obj.print_message()
print()



c_obj = C(3, 4, 5)
print(type(c_obj))
print('c_obj.a:', c_obj.a)
print('isinstance(c_obj, C):', isinstance(c_obj, C))
print('isinstance(c_obj, B):', isinstance(c_obj, B))
print('isinstance(c_obj, A):', isinstance(c_obj, A))

# check if the 'C' - class is a subclass of 'A' or 'B'
print('issubclass(C, (A, B)):', issubclass(C, (A, B)))

print('c_obj.b:', c_obj.b)
print('c_obj.c:', c_obj.c)
print('c_obj.in_A:', c_obj.in_A)
c_obj.print_message()
print()

A.print_message(c_obj)
B.print_message(c_obj)
C.print_message(c_obj)