"""Immutable Sequence Types"""

immut_seq = (1,2,3)
print(f"hash(immut_seq): {hash(immut_seq)}")
d = {immut_seq: 1, 'b': 2, 'c': 3}
print(f"d: {d}")

"""Attempting to hash an immutable sequence that contains unhashable values will result in TypeError."""
try:
    hash(([4,5,6], 7, 8, 9))
except TypeError as e:
    print(repr(e))