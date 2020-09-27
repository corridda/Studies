from math import pi, sin

# Generator expressions are more compact but less versatile than full generator definitions
# and tend to be more memory friendly than equivalent list comprehensions.

# sum of squares
print(f'sum(i*i for i in range(10)): {sum(i * i for i in range(10))}')

xvec = [10, 20, 30]
yvec = [7, 5, 3]

# dot product
print('\nsum(x * y for x, y in zip(xvec, yvec)):', sum(x * y for x, y in zip(xvec, yvec)))
print('type(x * y for x, y in zip(xvec, yvec):', type(x * y for x, y in zip(xvec, yvec)))

sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
print('\nsine_table:', sine_table)
print('type((x * pi / 180) for x in range(0, 91)):', type((x * pi / 180) for x in range(0, 91)))
print('type(sine_table):', type(sine_table))
print()

# compare the implementation of the generator expression and the list comprehension
data = 'golf'
print('data:', data)

# generator expression
print('type(data[i] for i in range(len(data) - 1, -1, -1)):', type(data[i] for i in range(len(data) - 1, -1, -1)))
x = list(data[i] for i in range(len(data) - 1, -1, -1))
print('x:', x)
print('type(x):', type(x))
y = "".join(data[i] for i in range(len(data) - 1, -1, -1))
print('y:', y)
print('type(y):', type(y))

# list comprehension
z = [data[i] for i in range(len(data) - 1, -1, -1)]
print('\nz:', z)
print('type(z):', type(z))
