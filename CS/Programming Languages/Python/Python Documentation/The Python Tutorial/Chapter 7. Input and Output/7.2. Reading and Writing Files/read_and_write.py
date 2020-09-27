# It is good practice to use the 'with' keyword when dealing with file objects
with open('text.txt', 'w') as f:
    f.write('string\n')
    f.write('new string\n')
    f.write('another string\n')
print('f.closed:', f.closed, '\n')

with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')
print('\nf.closed:', f.closed)

# error [ValueError: I/O operation on closed file.]
try:
    f.read()
except ValueError as e:
    print(e)