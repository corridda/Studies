class Dog:

    kind = 'canine'             # class variable shared by all instances

    tricks = []                 # mistaken use of a class variable

    def __init__(self, name):
        self.name = name        # instance variable unique to each instance

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

# shared by all dogs
print('d.kind: ', d.kind)
print('e.kind: ', e.kind)

# unique to each dog
print('d.name:', d.name)
print('e.name:', e.name)

d.add_trick('roll over')
e.add_trick('play dead')

print('d.tricks:', d.tricks)     # unexpectedly shared by all dogs