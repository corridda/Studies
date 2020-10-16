# The random module provides tools for making random selections.

import random

# random.choice(seq) [Choose a random element from a non-empty sequence.]
print("random.choice(['apple', 'pear', 'banana']):", random.choice(['apple', 'pear', 'banana']))
print("random.choice(['apple', 'pear', 'banana']):", random.choice(['apple', 'pear', 'banana']))
print("random.choice(['apple', 'pear', 'banana']):", random.choice(['apple', 'pear', 'banana']))

# random.sample(population, k) [Chooses k unique random elements from a population sequence or set.]
# sampling without replacement
print('random.sample(range(100), 10):', random.sample(range(100), 10))

# random float
print('random.random():', random.random())

# random.randrange(start, stop[, step]) [Choose a random item from range(start, stop[, step])]
print('random.randrange(6):', random.randrange(10, 20))