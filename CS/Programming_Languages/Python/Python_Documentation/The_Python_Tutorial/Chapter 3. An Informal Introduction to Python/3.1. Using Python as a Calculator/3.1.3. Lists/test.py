# Lists might contain items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
print('squares:', squares)
print('type(squares):', type(squares))

# Like strings (and all other built-in sequence type), lists can be indexed and sliced:
print('squares[0]:', squares[0])   # indexing returns the item
print('squares[-1]:', squares[-1])
print('squares[2:5]:', squares[2:5])

# Slicing returns a new list
# All slice operations return a new list containing the requested elements.
squares_new = squares[:]
print('squares_new:', squares_new)
print('id(squares):', id(squares))
print('id(squares_new):', id(squares_new))

# Lists also support operations like concatenation:
print(squares + [36, 49, 64, 81, 100])

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print('4 ** 3 = ', 4 ** 3)
cubes[3] = 4 ** 3   # replace the wrong value
print('cubes:', cubes)

# You can also add new items at the end of the list, by using the append() method
cubes.append(6 ** 3)    # add the cube of 6
cubes.append(7 ** 3)    # and the cube of 7
print('cubes:', cubes)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('letters:', letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print('letters:', letters)
# now remove them
letters[2:5] = []
print('letters:', letters)
# clear the list by replacing all the elements with an empty list
letters[:] = {}
print('letters:', letters)

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print('len(letters):', len(letters))

# It is possible to nest lists (create lists containing other lists), for example
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print('x:', x)
print('x[0]:', x[0])
print('x[0][1]:', x[0][1])