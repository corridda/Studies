class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return 'Hello world!'

print(MyClass.__doc__)

print('MyClass.i =', MyClass.i)
MyClass.i = 100
print('new MyClass.i =', MyClass.i)

print('\nMyClass.f =', MyClass.f)
print('MyClass().f():', MyClass().f())
print('MyClass.f(MyClass()):', MyClass.f(MyClass()))
x = MyClass()
print('x.f():', x.f())

print(f'\ntype(MyClass): {type(MyClass)}')
print(f'type(x): {type(x)}')
print(f'id(MyClass): {id(MyClass)}')
print(f'id(x): {id(x)}')

