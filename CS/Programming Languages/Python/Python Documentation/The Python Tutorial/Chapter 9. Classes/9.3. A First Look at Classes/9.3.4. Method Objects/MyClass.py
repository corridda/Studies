class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return 'Hello world!'


x = MyClass()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# 'x.f' is a method object
print('"x.f" is a method object:', x.f)

# method can be called
print('"x.f()":', x.f())

# it can also be stored away and called at a later time
xf = x.f
print(f'xf(): {xf()}')

