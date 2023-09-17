"""@staticmethod"""
# https://www.programiz.com/python-programming/methods/built-in/staticmethod

"""Transform a method into a static method.
The syntax of staticmethod() is:
    staticmethod(function)
Using staticmethod() is considered un-Pythonic way of creating a static function.
So, in newer versions of python, you can use the python decorator @staticmethod.
The syntax of @staticmethod is:
    @staticmethod
    def func(args, ...)

What is a static method?
Static methods, much like class methods, are methods that are bound to a class rather than its object.

They do not require a class instance creation. So, are not dependent on the state of the object.

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters.
Class method works with the class since its parameter is always the class itself.
They can be called both by the class and its object.

Class.staticmethodFunc()
or even
Class().staticmethodFunc()
"""



# Example 1: Create a static method using staticmethod()

class Mathematics:
    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print(f'The sum is: {Mathematics.addNumbers(5, 10)}\n')




"""When do you use static method?
1. Grouping utility function to a class
Static methods have very limited use case, because like class methods or any other methods within a class,
they cannot access properties of the class itself.
However, when you need a utility function that doesn't access any properties of a class
but makes sense that it belongs to the class, we use static functions."""



# Example 2: Create utility function as a static method

class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == dateWithDash):
    print(f"Equal\n")
else:
    print(f"Unequal\n")



"""2. Having a single implementation
Static methods are used when we don't want subclasses of a class change/override
a specific implementation of a method."""


# Example 3: How inheritance works with static method?

class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)


date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if (date.getDate() == dateFromDB.getDate()):
    print(f"Equal\n")
else:
    print(f"Unequal\n")

"""Here, we wouldn't want the subclass DatesWithSlashes to override the static utility
method toDashDate because it only has a single use, i.e. change date to dash-dates.

We could easily use the static method to our advantage by overriding getDate() method in the subclass
so that it works well with the DatesWithSlashes class."""
