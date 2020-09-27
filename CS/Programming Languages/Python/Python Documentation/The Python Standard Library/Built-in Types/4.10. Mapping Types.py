"""Mapping Types — dict"""

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(f"a == b == c == d == e: {a == b == c == d == e}\n")


"""These are the operations that dictionaries support (and therefore, custom mapping types should support too):"""

# len(d)
print(f"a: {a}")
print(f"len(a): {len(a)}")


# d[key]  // Raises a KeyError if key is not in the map.
try:
    print(f"a['two']: {a['two']}")
    print(f"a['five']: {a['five']}")
except KeyError as e:
    print(repr(e))
print()

"""If a subclass of dict defines a method __missing__() and key is not present,
the d[key] operation calls that method with the key key as argument. The d[key] operation then returns or raises
whatever is returned or raised by the __missing__(key) call. No other operations or methods invoke __missing__().
If __missing__() is not defined, KeyError is raised. __missing__() must be a method;
it cannot be an instance variable:"""

class Counter(dict):
    def __missing__(self, key):
        return 0
c = Counter()
print(f"c['red']: {c['red']}")
c['red'] += 1
print(f"c['red']: {c['red']}")
print(f"c: {c}\n")


# d[key] = value
a['four'] = 4
print(f"a: {a}\n")


# del d[key]
del  a['four']
print(f"a: {a}\n")


# key in d
print(f"'three' in a: {'three' in a}")
print(f"'five' in a: {'five' in a}\n")


# key not in d
print(f"'three' not in a: {'three' not in a}")
print(f"'five' not in a: {'five' not in a}\n")


# iter(d)
for i in iter(a):
    print(f"a['{i}']: {a[i]}")
print()


# clear()
a.clear()
print(f"a after clearing: {a}\n")
a = dict(one=1, two=2, three=3)


# copy()
print(f"a: {a}")
b = a.copy()
print(f"b: {b}\n")


# classmethod fromkeys(seq[, value])
b = dict.fromkeys(('four','five','six'), 0)
print(f"b: {b}\n")


# get(key[, default])  // this method never raises a KeyError.
print(f"a.get('three', None): {a.get('three', None)}")
print(f"a.get('four', None): {a.get('four', None)}\n")


# items()
for item in a.items():
    print(f"{item[0]}: {item[1]}")
print()


# keys()
print(f"a.keys(): {a.keys()}\n")


# pop(key[, default])
# If default is not given and key is not in the dictionary, a KeyError is raised.
try:
    print(f"a.pop('four', None): {a.pop('four', None)}")
    print(f"a.pop('five'): {a.pop('five')}")
except KeyError as e:
    print(repr(e))
print()


# popitem()  // Pairs are returned in LIFO order.
print(f"a: {a}")
while len(a):
    print(f"a.popitem(): {a.popitem()}")
print()


# setdefault(key[, default])
a = dict(one=1, two=2, three=3)
print(f"a: {a}")
print(f"a.setdefault('four', 4): {a.setdefault('four', 4)}")
print(f"a: {a}")
print(f"a.setdefault('four'): {a.setdefault('four')}")
print(f"a: {a}\n")


# update([other])
a.update(five=5, six=6)
print(f"a: {a}\n")


# values()
print(f"a.values(): {a.values()}\n")


"""Dictionaries preserve insertion order. Note that updating a key does not affect the order.
Keys added after deletion are inserted at the end."""
del a['two']
a['two'] = None
print(f"a: {a}\n")




"""Dictionary view objects"""

"""The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
Dictionary views can be iterated over to yield their respective data, and support membership tests:"""

# len(dictview)
print(f"len(a): {len(a)}")
print(f"len(a.items()): {len(a.items())}\n")

# iter(dictview)
for i in iter(a.items()):
    print(i)
print()

# x in dictview
print(f"'one' in a.keys(): {'one' in a.keys()}\n")


"""An example of dictionary view usage:"""
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# iteration
n = 0
for val in values:
    n += val
print(f"n: {n}")

# keys and values are iterated over in the same order (insertion order)
print(f"list(keys): {list(keys)}")
print(f"list(values): {list(values)}\n")

# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
print(f"list(keys): {list(keys)}\n")

# set operations
intersextion = keys & {'eggs', 'bacon', 'salad'}
print(f"keys & set(['eggs', 'bacon', 'salad']): {intersextion}\n")

symmetric_difference = keys ^ {'sausage', 'juice', 'bacon'}
print(f"keys ^ set(['sausage', 'juice', 'bacon']): {symmetric_difference}")

