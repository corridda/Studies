"""The heapq module provides functions for implementing heaps base."""

from heapq import heapify, heappop, heappush
import heapq

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                               # rearrange the list into heap order
print(f'data: {data}')
heappush(data, -5)                          # add a new entry
print([heappop(data) for i in range(3)])    # fetch the three smallest entries
print(f'data: {data}')
print(f'heappop(data): {heappop(data)}\n')

heappush(data, 2)
print(f'data: {data}')

# The lowest valued entry is always kept at position zero.
for i in range(len(data)):
    print(f'heappop(data): {heappop(data)}')

print(f"\nheapq.__all__: {heapq.__all__}")