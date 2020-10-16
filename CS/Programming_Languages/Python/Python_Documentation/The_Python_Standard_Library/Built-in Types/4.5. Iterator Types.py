"""Iterator Types"""

"""One method needs to be defined for container objects to provide iteration support:
    container.__iter__()
Return an iterator object. The object is required to support the iterator protocol described below.
The iterator objects themselves are required to support the following two methods, which together form
the iterator protocol:
    iterator.__iter__()
Return the iterator object itself. This is required to allow both containers and iterators to be used
with the for and in statements. This method corresponds to the tp_iter slot of the type structure for
Python objects in the Python/C API.
    iterator.__next__()
Return the next item from the container. If there are no further items, raise the StopIteration exception.
This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.
"""


class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        return iter([self.a, self.b, self.c])


class iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index += 1
        return self.data[self.index - 1]


class B:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        return iterator([self.a, self.b, self.c])


inst_A = A(3, 2, 1)
inst_B = A(6, 5, 4)

for el in inst_A:
    print(f"{el}")
print()

for el in inst_B:
    print(f"{el}")
print()


"""Python’s generators provide a convenient way to implement the iterator protocol.
If a container object’s __iter__() method is implemented as a generator, it will automatically return
an iterator object (technically, a generator object) supplying the __iter__() and __next__() methods.
More information about generators can be found in the documentation for the yield expression."""

class C:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        # generator
        for el in [self.a, self.b, self.c]:
            yield el

inst_C = A(9, 8, 7)

for el in inst_C:
    print(f"{el}")
print()