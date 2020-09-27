"""
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.
It generates arithmetic progressions:
"""

for i in range(5):
    print(i, '', end='')
print()

for i in range(5, 11):
    print(i, '', end='')
print()

for i in range(-10, -100, -30):
    print(i, '', end='')
print('\n')

# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print()

# A strange thing happens if you just print a range:
print(type(range(10)))
print(range(10))

# The function list() is another; it creates lists from iterables:
print('list(range(10)):', list(range(5)), '\n')

for i in range(10):
    print(i, '', end='')
print()

# reversed sequence
for i in range(10).__reversed__():
    print(i, '', end='')
print()
print(type(range(10).__reversed__()))