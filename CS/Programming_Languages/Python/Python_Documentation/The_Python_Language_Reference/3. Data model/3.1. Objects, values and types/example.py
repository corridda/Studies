a = 5
b = 5
c = 10

# The ‘is’ operator compares the identity of two objects.
print(f"a is b: {a is b}")
print(f"a is c: {a is c}\n")

# The id() function returns an integer representing its identity.
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}\n")

# The type() function returns an object’s type (which is an object itself).
# Like its identity, an object’s type is also unchangeable.
print(f"type(a): {type(a)}\n")