# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary.
# Note that duplicates have been removed.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('type(basket):', type(basket))
print('basket:', basket)
basket = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
print('type(basket):', type(basket))
print('basket:', basket)

print("\n'orange' in basket:", 'orange' in basket)
print("'strawberry' in basket:", 'strawberry' in basket)


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

# unique letters in a
print('\na =', a, type(a))
print('b =', b, type(b))

# letters in 'a' but not in 'b'
print("letters in 'a' but not in 'b':", a - b)

# letters in either 'a' or 'b'
print("letters in either 'a' or 'b':", a | b)

# letters in both 'a' and 'b'
print("letters in both 'a' and 'b':", a & b)

# letters in 'a' or 'b' but not both
print("letters in 'a' or 'b' but not both:", a ^ b)
# or like this
print("letters in 'a' or 'b' but not both:", (set.union(a, b)) - (a & b))

# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra'}
print(f'\na = {a}, type(a) = {type(a)}')
a = {x for x in 'abracadabra' if x not in 'abc'}
print(f'a = {a}, type(a) = {type(a)}')