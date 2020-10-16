"""super([type[, object-or-type]])"""
# https://www.programiz.com/python-programming/methods/built-in/super

"""Return a proxy object that delegates method calls to a parent or sibling class of type.
This is useful for accessing inherited methods that have been overridden in a class.
The search order is same as that used by getattr() except that the type itself is skipped.
If the second argument is omitted, the super object returned is unbound. If the second argument is an object,
isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type)
must be true (this is useful for classmethods).

In Python, super() built-in has two major use cases:
* Allows us to avoid using base class explicitly
* Working with Multiple Inheritance"""


# Example 1: super() with Single Inheritance
# In case of single inheritance, it allows us to refer base class by super().

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()
print()

"""Since, we do not need to specify the name of the base class if we use super(),
we can easily change the base class for Dog method easily (if we need to)."""

# changing base class to CanidaeFamily
class CanidaeFamily(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')

class Dog(CanidaeFamily):
  def __init__(self):
    print('Dog has four legs.')

    # no need to change this
    super().__init__('Dog')

d2 = Dog()
print()


"""The super() builtin returns a proxy object, a substitute object that has ability to call method of the base class
via delegation. This is called indirection (ability to reference base object with super())

Since the indirection is computed at the runtime, we can use point to different base class at different time
(if we need to)."""



# Example 2: super() with Multiple Inheritance

class Animal:
    def __init__(self, animalName):
        print(animalName, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammalName):
        print(NonWingedMammalName, "can't fly.")
        super().__init__(NonWingedMammalName)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammalName):
        print(NonMarineMammalName, "can't swim.")
        super().__init__(NonMarineMammalName)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')
print()

from pprint import pprint
pprint(Dog.__mro__)



"""Method Resolution Order (MRO)
It's the order in which method should be inherited in the presence of multiple inheritance.
You can view the MRO by using __mro__ attribute.

>>> Dog.__mro__
(<class 'Dog'>, 
<class 'NonMarineMammal'>, 
<class 'NonWingedMammal'>, 
<class 'Mammal'>, 
<class 'Animal'>, 
<class 'object'>)
Here is how MRO is calculated in Python:

A method in the derived calls is always called before the method of the base class.
In our example, Dog class is called before NonMarineMammal or NoneWingedMammal.
These two classes are called before Mammal which is called before Animal, and Animal class is called before object.
If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal),
method of NonMarineMammal is invoked first because it appears first."""