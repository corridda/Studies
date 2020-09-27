"""class property(fget=None, fset=None, fdel=None, doc=None)"""
# https://www.programiz.com/python-programming/methods/built-in/property

"""Return a property attribute.
'fget' is a function for getting an attribute value.
'fset' is a function for setting an attribute value.
'fdel' is a function for deleting an attribute value.
And 'doc' creates a docstring for the attribute.
"""


# A typical use is to define a managed attribute x:
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


"""If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.
If given, 'doc' will be the docstring of the property attribute.
Otherwise, the property will copy fget’s docstring (if it exists).
This makes it possible to create read-only properties easily using property() as a decorator:
"""
class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    """The @property decorator turns the voltage() method into a “getter”
    for a read-only attribute with the same name, and it sets the docstring for voltage to
    “Get the current voltage.”"""


"""A property object has getter, setter, and deleter methods usable as decorators that create a copy
of the property with the corresponding accessor function set to the decorated function.
This is best explained with an example:"""
class D:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class Person:
    # Here, _name is used as the private variable for storing the name of a Person.
    def __init__(self, name):
        self._name = name

    # We also set:
    # a getter method getName() to get the name of the person,
    # a setter method setName() to set the name of the person,
    # a deleter method delName() to delete the name of the person.
    def getName(self):
        print('Getting name')
        return self._name

    def setName(self, value):
        print('Setting name to ' + value)
        self._name = value

    def delName(self):
        print('Deleting name')
        del self._name

    # Set property to use getName, setName
    # and delName methods
    name = property(getName, setName, delName, 'Name property')

# Instead of using the property() method, you can use the Python decorator @property
# to assign the getter, setter and deleter.
class Person_2:
    def __init__(self, name):
        self._name = name

    # Here, instead of using the property() method, we've used the @property decorator.
    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


if __name__ == '__main__':
    c = C()
    print(f"c.x: {c.x}")
    c.x = 1
    print(f"c.x: {c.x}\n")

    parrot = Parrot()
    print(f"parrot.voltage: {parrot.voltage}\n")

    d = D()
    print(f"d.x: {d.x}")
    d.x = 2
    print(f"d.x: {d.x}")
    del d.x
    try:
        print(f"d.x: {d.x}")
    except AttributeError as e:
        print(repr(e))
    print()


    # Example 1: Create attribute with getter, setter and deleter using property()
    p = Person('Adam')
    print(f"p.name: {p.name}")
    p.name = 'John'
    del p.name
    print()


    # Example 2: Create attribute with getter, setter and deleter using @property decorator
    p = Person_2('Adam')
    print('The name is:', p.name)
    p.name = 'John'
    del p.name
