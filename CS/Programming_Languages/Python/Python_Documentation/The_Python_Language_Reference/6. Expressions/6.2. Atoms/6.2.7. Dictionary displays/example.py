# A dictionary display is a possibly empty series of key/datum pairs enclosed in curly braces.
# A dict comprehension, in contrast to list and set comprehensions, needs two expressions separated
# with a colon followed by the usual “for” and “if” clauses.
a = {}
b = {1: 10, 2: 20}
c = {x : int(str(x)+'0') for x in range(6)}
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"a: {type(a)}")
print(f"b: {type(b)}")
print(f"c: {type(c)}")

