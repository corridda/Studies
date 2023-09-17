"""https://t.me/pythonetc/232"""

"""Creating a new variable is essentially creating a new name for an already existing object.
That's why it's called name binding in python.
There are numerous ways to bind names, these are the examples of how x can be bind:"""

"""
x = y
import x

class x: pass

def x(): pass

def y(x): pass

for x in y: pass

with y as x: pass
except y as x:
"""

# You also can bind an arbitrary name by manipulating global namespaces:
try:
    print(f"x: {x}")
except NameError as e:
    print(repr(e))
globals()['x'] = 42
print(f"x: {x}\n")
print(f"globals():\n{globals()}")

# Note, however, that you cannot do the same with locals() since updates to the locals dictionary are ignored.