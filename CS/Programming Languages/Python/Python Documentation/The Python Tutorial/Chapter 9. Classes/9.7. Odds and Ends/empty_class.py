# Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”,
# bundling together a few named data items.

class Employee:
    pass


John = Employee()
John.name = 'John'
John.age = 56
John.salary = 75000

print('John.name:', John.name)
print('John.age:', John.age)
print('John.salary:', John.salary)