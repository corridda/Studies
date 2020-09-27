# you can loop over a sequence using a for statement:
for element in "abc":
    print(element, '', end='')
print('\n')

# iter()
s = 'abc'
it = iter(s)
print('type(it):', type(it))
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print('Values have ceased.')

