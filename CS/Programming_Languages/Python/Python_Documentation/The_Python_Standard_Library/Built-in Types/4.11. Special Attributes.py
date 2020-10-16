"""Special Attributes"""

# object.__dict__
print(f"list.__dict__:\n{list.__dict__}\n")


# instance.__class__
class A:
    pass

a = A()
print(f"a.__class__: {a.__class__}\n")


# class.__bases__
class B(A):
    pass

class C(B):
    pass

print(f"C.__bases__: {C.__bases__}")
print(f"C.__bases__[0].__bases__: {C.__bases__[0].__bases__}\n")



# definition.__name__
gen = (x for x in range(1,11))
gen.__name__ = 'Generator of the sequence of integers from 1 to 10'
print(f"gen.__name__: {gen.__name__}\n")


# definition.__qualname__
class C:
    class D:
        def meth(self):
            pass
print(f"C.D.meth.__qualname__: {C.D.meth.__qualname__}\n")



# class.__mro__
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(C, B):
    pass

print(f"B.__mro__: {B.__mro__}")
print(f"D.__mro__: {D.__mro__}")



# class.mro()
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(C, B):
    @classmethod
    def mro(cls):
        return (D, B, C, A)

print(f"D().mro(): {D().mro()}\n")



# class.__subclasses__()
print(f"int.__subclasses__(): {int.__subclasses__()}")
print(f"A.__subclasses__(): {A.__subclasses__()}")
