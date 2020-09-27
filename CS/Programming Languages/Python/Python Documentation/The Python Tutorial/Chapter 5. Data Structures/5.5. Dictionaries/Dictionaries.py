# A pair of braces creates an empty dictionary: {}.
empty_dic = {}
print(f"empty_dic: {empty_dic}, type(empty_dic): {type(empty_dic)}")

# Placing a comma-separated list of key:value pairs within the braces
# adds initial key:value pairs to the dictionary/
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print('\ntel =', tel, type(tel))
print("tel['jack'] =", tel['jack'])

del tel['sape']
tel['irv'] = 4127
print('tel =', tel, type(tel))
print(f"check if 'sape' is in the 'tel': {'sape' in tel}")

# It is an error to extract a value using a non-existent key.
try:
    print(f"tel['sape']: {tel['sape']}")
except KeyError as e:
    print('KeyError', e)

# list of keys
list_of_keys = list(tel.keys())
print(f'\nlist_of_keys: {list_of_keys}')

# or using the list comprehension
list_of_keys = [x for x in tel.keys()]
print(f'list_of_keys: {list_of_keys}')

# sorted list of keys
sorted_list_of_keys = sorted(tel.keys())
print('sorted_list_of_keys =', sorted_list_of_keys)

# check that 'guido' is in 'tel'
print("'guido' in tel:", 'guido' in tel)

# The dict() constructor
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# dict comprehensions
b = {x: x**2 for x in [2,3,4]}
print('b =', b, type(b))

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
c = dict(sape=4139, guido=4127, jack=4098)
print('c =', c, type(c))

# Calling d.keys() will return a dictionary view object.
# It supports operations like membership test and iteration,
# but its contents are not independent of the original dictionary – it is only a view.
print(f'\ntype(c.keys()): {type(c.keys())}')
print(f'c.keys(): {c.keys()}')


