# Lambda functions can be used wherever function objects are required.
a, b = 10, 5
print('(lambda  a, b: a + b):', lambda  a, b: a + b)
print((lambda  a, b: a + b)(a, b))
(lambda  a, b: print(a + b))(a, b)


# Like nested function definitions, lambda functions can reference variables from the containing scope:
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))     # == (lambda x: x + 42)(0)
print(f(1))     # == (lambda x: x + 43)(0)

# Another use is to pass a small function as an argument:
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
print('pairs:', pairs)
pairs.sort(key=lambda pair: pair[1])
print('pairs:', pairs)

# print('The sum of your nums is:',\
#       (lambda a, b: a + b)(int(input('Enter the first num:\n')), int(input('Enter the second num:\n'))), '\n')

# (lambda x = int(input('Enter the num:\n')), y = int(input('Enter the power:\n')):\
#     print(f'{x} ** {y} = {x ** y}'))()

(lambda x, y: print(f'{x} ** {y} = {x ** y}'))\
    (int(input('Enter the num:\n')),int(input('Enter the power:\n')))