"""Ranges"""

"""The range type represents an immutable sequence of numbers and is commonly used for looping
a specific number of times in for loops.

class range(stop)class range(start, stop[, step])
The arguments to the range constructor must be integers (either built-in int or any object that implements
the __index__ special method). If the step argument is omitted, it defaults to 1.
If the start argument is omitted, it defaults to 0. If step is zero, ValueError is raised.
"""

print(f"list(range(10)): {list(range(10))}")
print(f"list(range(1, 11)): {list(range(1, 11))}")
print(f"list(range(0, 30, 5)): {list(range(0, 30, 5))}")
print(f"list(range(0, 10, 3)): {list(range(0, 10, 3))}")
print(f"list(range(0, -10, -1)): {list(range(0, -10, -1))}")
print(f"list(range(0)): {list(range(0))}")
print(f"list(range(1, 0)): {list(range(1, 0))}\n")

"""The advantage of the range type over a regular list or tuple is that a range object will always take
the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start,
stop and step values, calculating individual items and subranges as needed)."""
print(f"[x for x in range(10**3)].__sizeof__(): {[x for x in range(10 ** 3)].__sizeof__()}")
print(f"range(10**9).__sizeof__(): {range(10 ** 3).__sizeof__()}\n")

r = range(0, 20, 2)
print(f"11 in r: {11 in r}")
print(f"10 in r: {10 in r}")
print(f"r.index(10): {r.index(10)}")
print(f"r[5]: {r[5]}")
print(f"r[:5]: {r[:5]}")
print(f"r[-1]: {r[-1]}")
