a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

del a[0]
print(a)

del a[2:4]
print(a)

# clear 'a'
del a[:]
print(a)

# delete 'a'
del a
try:
    print(a)
except NameError as e:
    print(e)
