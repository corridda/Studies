"""Lists"""

"""class list([iterable])
    Lists may be constructed in several ways:
    •Using a pair of square brackets to denote the empty list: []
    •Using square brackets, separating items with commas: [a], [a, b, c]
    •Using a list comprehension: [x for x in iterable]
    •Using the type constructor: list() or list(iterable)
"""

print(f"['a','b','c'] == [x for x in 'abc'] == list('abc'): {['a','b','c'] == [x for x in 'abc'] == list('abc')}\n")


# sort(*, key=None, reverse=False)
"""sort() accepts two arguments that can only be passed by keyword (keyword-only arguments):
'key' specifies a function of one argument that is used to extract a comparison key from each list element
(for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used
for the entire sorting process. The default value of None means that list items are sorted directly
without calculating a separate key value.
'reverse' is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
"""

lst = [6,45,97,55,12,24,94,65,20,65]
print(f"lst: {lst}")
lst.sort()
print(f"lst after sorting: {lst}")

lst = [6,45,97,55,12,24,94,65,20,65]
lst.sort(reverse=True)
print(f"lst after sorting: {lst}")

lst = [6,45,97,55,12,24,94,65,20,65]
lst.sort(key=lambda x: x%2)
print(f"lst after sorting: {lst}")
