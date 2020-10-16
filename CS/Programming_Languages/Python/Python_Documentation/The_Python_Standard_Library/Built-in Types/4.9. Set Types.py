"""Set Types — set, frozenset"""

s = {1,2,3,4,5,6}
print(f"type(s): {type(s)}\n")


# len(s)
print(f"len(s): {len(s)}\n")


# x in s
print(f"3 in s: {3 in s}")
print(f"9 in s: {9 in s}\n")


# x not in s
print(f"3 not in s: {3 not in s}")
print(f"9 not in s: {9 not in s}\n")


# isdisjoint(other)
temp_1 = {4,5,6}
temp_2 = {7,8,9}
print(f"s: {s}")
print(f"temp_1: {temp_1}")
print(f"temp_2: {temp_2}")
print(f"s.isdisjoint(temp_1): {s.isdisjoint(temp_1)}")
print(f"s.isdisjoint(temp_2): {s.isdisjoint(temp_2)}\n")


# issubset(other) / set <= other
print(f"temp_1.issubset(s): {temp_1.issubset(s)}")
print(f"temp_1 <= s: {temp_1 <= s}")
print(f"temp_2.issubset(s): {temp_2.issubset(s)}")
print(f"temp_2 <= s: {temp_2 <= s}\n")


# set < other
temp_3 = {1,2,3,4,5,6}
print(f"temp_3: {temp_3}")
print(f"temp_1 < s: {temp_1 < s}")
print(f"temp_3 < s: {temp_3 < s}\n")


# issuperset(other) / set >= other
print(f"s: {s}")
print(f"temp_1: {temp_1}")
print(f"temp_2: {temp_2}")
print(f"s.issuperset(temp_1): {s.issuperset(temp_1)}")
print(f"s >= temp_1: {s >= temp_1}")
print(f"s.issuperset(temp_2): {s.issuperset(temp_2)}")
print(f"s >= temp_2: {s >= temp_2}\n")


# set > other
print(f"temp_3: {temp_3}")
print(f"s > temp_1: {s > temp_1}")
print(f"s > temp_3: {s > temp_3}\n")


# union(*others)
# set | other | ...
temp_4 = {10,11,12}
print(f"s: {s}")
print(f"temp_2: {temp_2}")
print(f"temp_4: {temp_4}")
print(f"s.union(temp_2, temp_4):\n{s.union(temp_2, temp_4)}")
print(f"s | temp_2 | temp_4:\n{s | temp_2 | temp_4}\n")


# intersection(*others)
# set & other & ...
temp_5 = {5,6,7,8,9,10}
print(f"s: {s}")
print(f"temp_5: {temp_5}")
print(f"s.intersection(temp_5):\n{s.intersection(temp_5)}")
print(f"s & temp_5:\n{s & temp_5}\n")


# difference(*others)
# set - other - ...
print(f"s.difference(temp_5):\n{s.difference(temp_5)}")
print(f"s - temp_5:\n{s - temp_5}\n")


# symmetric_difference(other)
# set ^ other
print(f"s: {s}")
print(f"temp_5: {temp_5}")
print(f"s.symmetric_difference(temp_5):\n{s.symmetric_difference(temp_5)}")
print(f"s ^ temp_5:\n{s ^ temp_5}\n")


# copy()
s_copy = s.copy()
print(f"s: {s}")
print(f"s_copy: {s_copy}\n")


"""Note, the non-operator versions of union(), intersection(), difference(), and symmetric_difference(),
issubset(), and issuperset() methods will accept any iterable as an argument.
In contrast, their operator based counterparts require their arguments to be sets.
This precludes error-prone constructions like set('abc') & 'cbs' in favor of the more readable
set('abc').intersection('cbs')."""
try:
    print(set('abc') & 'cbs')
except TypeError as e:
    print(repr(e))
print(f"set('abc').intersection('cbs'): {set('abc').intersection('cbs')}\n")


"""Both set and frozenset support set to set comparisons. Two sets are equal if and only if every element
of each set is contained in the other (each is a subset of the other).
A set is less than another set if and only if the first set is a proper subset of the second set
(is a subset, but is not equal). A set is greater than another set if and only if the first set
is a proper superset of the second set (is a superset, but is not equal)."""
print(f"s: {s}")
print(f"s_copy: {s_copy}")
print(f"s == s_copy: {s == s_copy}")
print(f"s < set([1,2,3,4,5,6,7,8,9]): {s < set([1,2,3,4,5,6,7,8,9])}")
print(f"s > set([1,2,3]): {s > set([1,2,3])}\n")


"""Binary operations that mix set instances with frozenset return the type of the first operand.
For example: frozenset('ab') | set('bc') returns an instance of frozenset."""
print(f"type(frozenset('ab') | set('bc')): {type(frozenset('ab') | set('bc'))}")
print(f"type(set('bc') | frozenset('ab')): {type(set('bc') | frozenset('ab'))}\n")



"""The following table lists operations available for set that do not apply to immutable instances of frozenset:"""

# update(*others)
# set |= other | ...
print(f"s: {s}")
print(f"temp_2: {temp_2}")
s.update(temp_2)
print(f"s after updating: {s}\n")


# intersection_update(*others)
# set &= other & ...
print(f"s: {s}")
print(f"temp_2: {temp_2}")
s.intersection_update(temp_2)
print(f"s after updating: {s}\n")


# difference_update(*others)
# set -= other | ...
print(f"s: {s}")
print(f"temp_2: {temp_2}")
s.difference_update(temp_2)
print(f"s after updating: {s}\n")


# symmetric_difference_update(other)
# set ^= other
s = {1,2,3,4,5,6}
print(f"s: {s}")
print(f"temp_5: {temp_5}")
s.symmetric_difference_update(temp_5)
print(f"s after updating: {s}\n")


# add(elem)
s.add(5)
s.add(6)
print(f"s after updating: {s}\n")


# remove(elem)
# Raises KeyError if elem is not contained in the set.
try:
    s.remove(6)
except KeyError as e:
    print(repr(e))
print(f"s after updating: {s}\n")


# discard(elem)
s.discard(5)
s.discard(11)
print(f"s after updating: {s}\n")


# pop()
# Raises KeyError if the set is empty.
temp_6 = set()
try:
    print(f"{temp_6.pop()}")
except KeyError as e:
    print(repr(e))
print()


# clear()
s.clear()
print(f"s after updating: {s}\n")


s = {1,2,3,4,5,6}
print(f"s:")
while len(s) > 0:
    print(s.pop(), end=' ')
