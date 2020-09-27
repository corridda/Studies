# An empty pair of parentheses yields an empty tuple object.
a = ()
b = ()
print(f"type(a): {type(a)}")
print(f"type(b): {type(b)}")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

# Note that tuples are not formed by the parentheses, but rather by use of the comma operator.
# The exception is the empty tuple.
a = 1, 2 ,3
print(f"a: {a}")
print(f"type(a): {type(a)}")

