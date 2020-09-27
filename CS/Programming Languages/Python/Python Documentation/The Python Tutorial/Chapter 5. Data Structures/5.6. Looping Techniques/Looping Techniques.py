import math

# looping through dictionaries -> items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, ':', v)

# looping through a sequence ->
# the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'The Holy Grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')

# To loop over a sequence in reverse, first specify the sequence in a forward direction
# and then call the reversed() function.
print('reversed list: ', end='')
for i in reversed([1, 2, 3]):
    print(i, '', end='')

# the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print('\nsorted list: ', end='')
for i in sorted(basket):
    print(i, '', end='')

# It is sometimes tempting to change a list while you are looping over it;
# however, it is often simpler and safer to create a new list instead
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print('\nsorted(filtered_data):', sorted(filtered_data))
print('filtered_data:', filtered_data)

# You can always simply delete the unnecessary data by 'del'
print(f'raw_data: {raw_data}')
del raw_data
try:
    print(f'raw_data: {raw_data}')
except NameError as e:
    print(e)
