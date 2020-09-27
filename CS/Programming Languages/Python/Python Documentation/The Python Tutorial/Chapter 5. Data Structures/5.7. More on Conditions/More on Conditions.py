# The operators is and is not compare whether two objects are really the same object
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)

b = a
print(id(a))
print(id(b))
print(a is b)

# It is possible to assign the result of a comparison or other Boolean expression to a variable.
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(f'\nnon_null = {non_null}')

