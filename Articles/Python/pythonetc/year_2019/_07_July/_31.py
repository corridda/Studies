"""https://t.me/pythonetc/429"""

"""You can slice dicts using dict comprehensions:"""
d = dict(a=1, b=2, c=3)

d1 = {k: d.get(k) for k in ['a', 'c', 'e']}
d2 = {k: d.get(k) for k in ['a', 'c', 'e'] if k in d}
d3 = {k: d.get(k) for k in d.keys() if k in {'a', 'c', 'e'}}

print(d1)
print(d2)
print(d3)
