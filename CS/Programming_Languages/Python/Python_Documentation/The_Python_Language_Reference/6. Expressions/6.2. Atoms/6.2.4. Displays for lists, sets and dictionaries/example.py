# The comprehension consists of a single expression followed by at least one for clause
# and zero or more for or if clauses.

a = [x**2 for x in range(11) if x % 2 == 0]
print(f"a: {a}")
print(f"type(a): {type(a)}")

