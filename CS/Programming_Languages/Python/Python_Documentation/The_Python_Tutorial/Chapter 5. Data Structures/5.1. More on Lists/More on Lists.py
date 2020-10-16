from collections import deque
from math import pi

# 5.1. Подробнее о списках
a = []
print('a:', a)

# L.append(object) -> None -- append object to end
a.append(1)
print('a:', a)

# L.extend(iterable) -> None -- extend list by appending elements from the iterable
a.extend([2, 3, 4, 5])
print('a:', a)

# L.insert(index, object) -- insert object before index
for i in [0, 1]:
    a.insert(0, -1)
print('a:', a)

# L.remove(value) -> None -- remove first occurrence of value.
# Raises ValueError if the value is not present.
for i in range(3):
    try:
        a.remove(-1)
    except ValueError:
        print(f"There's no such an element like '-1' in the list!")
    print('a:', a)

# L.pop([index]) -> item -- remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
print('a.pop(0):', a.pop(0))
print('a:', a)
try:
    print(a.pop(len(a)))
except IndexError:
    print("List is empty or index is out of range ")

# L.clear() -> None -- remove all items from L
a.clear()
print('a:', a)

# L.index(value, [start, [stop]]) -> integer -- return first index of value.
# Raises ValueError if the value is not present.
a = list(range(1,6))
print('a:', a)
try:
    print('a.index(4):', a.index(4))
    print('a.index(5):', a.index(6))
except ValueError:
    print('There\'s no such an element!')

# L.count(value) -> integer -- return number of occurrences of value
for i in range(3):
    a.insert(0, -1)
print('a:', a)
print('a.count(-1):', a.count(-1))

# L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
a.sort(reverse=True)
print('a:', a)

# L.reverse() -- reverse *IN PLACE*
a.reverse()
print('a:', a)

# L.copy() -> list -- a shallow copy of L
b = a.copy()
print('\nlist.copy()')
print('b:', b)
a.reverse()
print('a:', a)
print("'b' wasn't changed:", b)
a.clear()
print('a:', a)
print("'b' wasn't changed:", b)



""" --- 5.1.1. Using Lists as Stacks --- """

stack = [3, 4, 5]
print('\nstack:', stack)

# appending on the top of the stack
stack.append(6)
stack.append(7)
print('stack:', stack)

# popping from the top of the stack
print('stack.pop(): ', stack.pop())
print('stack:', stack)



""" --- 5.1.2. Using Lists as Queues --- """

# collections.deque
queue = deque(['Бабушка', 'Дедушка'])
print('\nqueue:', queue)

queue.extend(['Игорь', 'Ирина', 'Вика', 'Гриша'])
print('queue:', queue)

print('queue.popleft():', queue.popleft())
print('queue.popleft():', queue.popleft())
print('queue:', queue)

queue.extendleft(['Бабушка', 'Дедушка'])
print("'Бабушка' and 'Дедушка' are with us again!")
print('queue:', queue)

queue.rotate(4)
print('queue:', queue)



""" --- 5.1.3. List Comprehensions --- """

squares = [x ** 2 for x in range(10)]
print('\nsquares:', squares)

combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print('combs:', combs)

# all the same
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print('combs:', combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
doubled_vec = [x * 2 for x in vec]
print('doubled_vec:', doubled_vec)

# filter the list to exclude negative numbers
filtered_vec = [x for x in vec if x >= 0]
print('filtered_vec:', filtered_vec)

# apply a function to all the elements
abs_vec = [abs(x) for x in vec]
print('abs_vec:', abs_vec)

# call a method on each element
fruits = ['   banana', 'apple   ', '   plum     ']
print('stripped_fruits', [f.strip() for f in fruits])

# create a list of 2-tuples like (number, square)
# the tuple must be parenthesized, otherwise an error is raised
print('nums_and_squares: ', [(x, x ** 2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('flattened_vec', [num for elem in vec for num in elem])

# List comprehensions can contain complex expressions and nested functions:
print('rounded pi:', [str(round(pi, i)) for i in range(6)])



""" --- 5.1.4. Nested List Comprehensions --- """

# matrix is a list 3 x 4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print('\nmatrix:', matrix)

# transposition
print('transposed_matrix', [[row[i] for row in matrix] for i in range(4)])

# all the same
transposed_matrix = []
for i in range(4):
    transposed_matrix.append([row[i] for row in matrix])
print('transposed_matrix', transposed_matrix)

# all the same
transposed_matrix = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)
print('transposed_matrix', transposed_matrix)

# zip() []
print('list(zip(*matrix)):', list(zip(*matrix)))
