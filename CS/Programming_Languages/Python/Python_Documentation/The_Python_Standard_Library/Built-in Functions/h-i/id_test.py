"""id(object)"""
# https://www.programiz.com/python-programming/methods/built-in/id

"""Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant
for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
CPython implementation detail: This is the address of the object in memory.
"""


class Foo:
    b = 5


a = 'abc'
b = 'def'
print(f"id(a): {id(a)},\nid(b): {id(b)}")
dummyFoo = Foo()
print(f'id of dummyFoo = {id(dummyFoo)}\n')

print('id of 5 =',id(5))

a = 5
print('id of a =',id(a))

b = a
print('id of b =',id(b))

c = 5.0
print('id of c =',id(c))

"""It's important to note that everything in Python is an object, even numbers and Classes.
Hence, integer 5 has a unique id. The id of the integer 5 remains constant during the lifetime.
Similar is the case for float 5.5 and other objects."""