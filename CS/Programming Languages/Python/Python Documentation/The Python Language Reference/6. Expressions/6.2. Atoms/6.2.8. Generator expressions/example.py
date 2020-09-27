# A generator expression is a compact generator notation in parentheses.
# A generator expression yields a new generator object.
a = (x**2 for x in range(6))
print(f"a: {a}")
print(f"type(a): {type(a)}")

for i in a:
    print(i)
