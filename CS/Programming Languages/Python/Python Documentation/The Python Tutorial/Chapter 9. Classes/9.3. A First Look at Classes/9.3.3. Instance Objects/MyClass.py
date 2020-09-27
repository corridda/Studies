class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return 'Hello world!'

x = MyClass()

# data attributes
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print('x.counter =', x.counter)
del x.counter

x.attribute = 15
print('x.attribute =', x.attribute)

# 'MyClass.f' is a function object
print('"MyClass.f" is a function object:', MyClass.f)

# 'x.f' is a method object
print('"x.f" is a method object:', x.f)

# method can be called
print('"x.f()":', x.f())

