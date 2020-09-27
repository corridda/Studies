"""@classmethod"""
# https://www.programiz.com/python-programming/methods/built-in/classmethod

"""Transform a method into a class method.
A class method receives the class as implicit first argument, just like an instance method receives the instance.
To declare a class method, use this idiom:
"""

# class C:
#     @classmethod
#     def f(cls, arg1, arg2, ...): ...

"""It can be called either on the class (such as C.f()) or on an instance (such as C().f())."""

# http://qaru.site/questions/10955/meaning-of-classmethod-and-staticmethod-for-beginner
"""@classmethod означает: когда этот метод вызывается, мы передаем класс как первый аргумент
вместо экземпляра этого класса (как обычно мы делаем с методами).
Это означает, что вы можете использовать класс и его свойства внутри этого метода, а не конкретный экземпляр.
@staticmethod означает: когда вызывается этот метод, мы не передаем ему экземпляр класса
(как это обычно делается с методами). Это означает, что вы можете поместить функцию внутри класса,
но вы не можете получить доступ к экземпляру этого класса (это полезно, когда ваш метод не использует экземпляр)."""

from datetime import date


class A:
    @classmethod
    def class_method(cls):
        print("Inside class_method()")

    def instance_method(self):
        print("Inside instance_method()")


class Person_1:
    age = 25

    @classmethod
    # cls accepts the class Person as a parameter rather than Person's object/instance.
    def printAge(cls):
        print(f"The age is: {cls.age}")


# random Person
class Person_2:
    # Here, we have two class instance creator, a constructor and a fromBirthYear method.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


class Person_3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Here, using a static method to create a class instance wants us to hardcode the instance type during creation.
    # This clearly causes a problem when inheriting Person to Man.
    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person_3(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


class Man(Person_3):
    sex = 'Male'


def main():
    a = A()
    # The class method can be called both by the class and its object.
    A.class_method()
    # or even
    A().class_method()
    a.class_method()
    print()

    A.instance_method(a)
    a.instance_method()
    print()

    # We call printAge without creating a Person object like we do for static methods.
    Person_1.printAge()
    print()

    # Create factory method using class method
    person = Person_2('Adam', 19)
    person.display()
    person1 = Person_2.fromBirthYear('John', 1985)
    person1.display()
    print()

    # How class method works for inheritance?
    man = Man.fromBirthYear('John', 1985)
    print(f"isinstance(man, Man): {isinstance(man, Man)}")

    man1 = Man.fromFathersAge('John', 1965, 20)
    # fromFathersAge method doesn't return a Man object but its base class Person's object.
    print(f"isinstance(man1, Man): {isinstance(man1, Man)}")
    print(f"isinstance(man1, Person_3): {isinstance(man1, Person_3)}")

if __name__ == "__main__":
    main()
