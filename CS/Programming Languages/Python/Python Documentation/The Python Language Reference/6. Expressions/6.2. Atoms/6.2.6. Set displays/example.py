# A set display is denoted by curly braces and distinguishable from dictionary displays
# by the lack of colons separating keys and values:
a = {1, 2, 3}
b = {x**2 for x in range(11) if x % 2 == 0}
print(f"a: {a}")
print(f"b: {b}")
print(f"type(a): {type(a)}")
print(f"type(b): {type(b)}")
