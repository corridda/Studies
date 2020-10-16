# Methods may call other methods by using method attributes of the self argument:
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)


bag = Bag()
bag.add(10)
bag.add_twice(20)
print('bag.data:', bag.data)


# Data attributes override method attributes with the same name!!!
# To avoid accidental name conflicts, which may cause hard-to-find bugs in large programs,
# it is wise to use some kind of convention that minimizes the chance of conflicts.
Bag.add = 10
print('bag.add:', bag.add)


# Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.
print('bag.__class__:', bag.__class__)
