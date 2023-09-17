"""Common Sequence Operations"""

import time

def timed(f, *args, n_iter=10):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        acc = min(acc, time.perf_counter() - t0)
    return acc

def concatination_quadratic(content: list) -> str:
    res = ''
    for line in content:
        res += line
    return res

def concatination_linear(content: list) -> str:
    return ''.join(content)



# in, not in
lst = [1,2,3]
print(f"1 in lst: {1 in lst}")
print(f"10 in lst: {10 not in lst}")
print(f"'gg' in 'eggs': {'gg' in 'eggs'}\n")



# '+' (the concatenation of s and t)
lst_2 = [4,5,6]
print(f"lst + lst_2: {lst + lst_2}")

"""Concatenating immutable sequences always results in a new object. This means that building up a sequence
by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear
runtime cost, you must switch to one of the alternatives below:
◦if concatenating str objects, you can build a list and use str.join() at the end or else write
to an io.StringIO instance and retrieve its value when complete
◦if concatenating bytes objects, you can similarly use bytes.join() or io.BytesIO,
or you can do in-place concatenation with a bytearray object. bytearray objects are mutable and have
an efficient overallocation mechanism
◦if concatenating tuple objects, extend a list instead
◦for other types, investigate the relevant class documentation
"""
with open('История философии (2001).txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(f"quadratic runtime cost: {timed(concatination_quadratic, content)}")
    print(f"linear runtime cost: {timed(concatination_linear, content)}")
print()


# '*' (equivalent to adding s to itself n times)
print(f"[10] * 5: {[10] * 5}")
print(f"(1,2,3) * 3: {(1,2,3) * 3}")
print(f"list(range(1,6)) * 2: {list(range(1,6)) * 2}")
print(f"Euro* 5: {'Euro*' * 5}")

"""2.Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s).
Note that items in the sequence s are not copied; they are referenced multiple times.
This often haunts new python programmers; consider:"""
lists = [[]] * 3
print(f"lists: {lists}")
lists[0].append(3)
print(f"lists: {lists}")

"""What has happened is that [[]] is a one-element list containing an empty list, so all three elements
of [[]] * 3 are references to this single empty list. Modifying any of the elements of lists modifies
this single list. You can create a list of different lists this way:"""
lists = [[] for i in range(3)]
print(f"lists: {lists}")
lists[0].append(3)
lists[1].append(4)
lists[2].append(5)
print(f"lists: {lists}\n")



# slices
print(f"{lst[:3]}")
print(f"{lst[:3:2]}")
print(f"{lst[-1::-1]}\n")



# len(s) [length of s]
print(f"len(lst): {len(lst)}")



# min(s) [smallest item of s], max(s) [largest item of s]
print(f"min(lst): {min(lst)}\nmax(s: {max(lst)})\n")



# s.index(x[, i[, j]]) [index of the first occurrence of x in s (at or after index i and before index j)]
print(f"lst.index(3): {lst.index(3)}\n")



# s.count(x) [total number of occurrences of x in s]
lst = [1,2,3,3,3,3,3,4,5]
print(f"lst: {lst}")
print(f"lst.count(3): {lst.count(3)}")