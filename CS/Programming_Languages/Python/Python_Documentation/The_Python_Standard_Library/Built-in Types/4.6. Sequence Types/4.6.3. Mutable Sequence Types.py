"""Mutable Sequence Types"""

"""'s' is an instance of a mutable sequence type, 't' is any iterable object and 'x' is an arbitrary object
that meets any type and value restrictions imposed by 's'"""

lst = [1,2,3,4,5]


# s[i] = x  [item i of s is replaced by x]
print(f"{lst}")
lst[-1] = 10
print(f"lst: {lst}\n")


# s[i:j] = t  [slice of s from i to j is replaced by the contents of the iterable t]
lst[:3] = [10,20,30]
print(f"lst: {lst}\n")


# del s[i:j]  [same as s[i:j] = []]
del lst[:4]
print(f"lst: {lst}\n")


# s.append(x) [appends x to the end of the sequence (same as s[len(s):len(s)] = [x])]
lst.append(20)
lst.append(30)
print(f"lst: {lst}\n")


# s.clear()  [removes all items from s (same as del s[:])]
lst.clear()
print(f"lst after clearing: {lst}\n")


# s.copy()  [creates a shallow copy of s (same as s[:])]
lst.append(1)
lst.append(2)
lst.append(3)
lst.append([4,5,6])
lst_2 = lst.copy()
print(f"lst_2: {lst_2}")
print(f"lst: {lst}")
print(f"lst_2: {lst_2}")
lst_2[-1].append(7)
# Note that lst has also changed. This is because of shallow copy.
print(f"lst: {lst}")
print(f"lst_2: {lst_2}\n")


# s.extend(t) or s += t  [extends s with the contents of t]
lst = [1,2,3]
print(f"lst: {lst}")
lst.extend([4,5,6])
print(f"lst: {lst}\n")


# s *= n  [updates s with its contents repeated n times]
# Zero and negative values of n clear the sequence.
lst *= 2
print(f"lst: {lst}")
lst *= -1
print(f"lst: {lst}\n")


# s.insert(i, x)  [inserts x into s at the index given by i (same as s[i:i] = [x])]
lst = [1,2,3]
print(f"lst: {lst}")
lst.insert(0, 100)
print(f"lst: {lst}\n")


# s.pop([i])  [retrieves the item at i and also removes it from s]
# The optional argument i defaults to -1, so that by default the last item is removed and returned.
print(f"lst.pop(0): {lst.pop(0)}")
print(f"lst: {lst}\n")


# s.remove(x)  [remove the first item from s where s[i] is equal to x]
# remove raises ValueError when x is not found in s.
lst = [1,2,3,4,4,4,5]
print(f"lst: {lst}")
lst.remove(4)
print(f"lst: {lst}\n")


# s.reverse()  [reverses the items of s in place]
"""4.The reverse() method modifies the sequence in place for economy of space when reversing a large sequence.
To remind users that it operates by side effect, it does not return the reversed sequence."""
lst = [1,2,3,4,5]
print(f"lst: {lst}")
lst.reverse()
print(f"lst: {lst}\n")
