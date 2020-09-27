# read() [If the end of the file has been reached, f.read() will return an empty string ('').]
with open('text.txt', 'r') as f:
    print(f.read())

# f.readline()
with open('text.txt', 'r') as f:
    print(f.readline(), end='') # first line
    print(f.readline(), end='') # second line
    print(f.readline(), end='') # third line
    print(f.readline(), end='') # no more lines [EOF]
print()

# looping over the file object
with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')
print()

# read all the lines of a file in a list
with open('text.txt', 'r') as f:
    list = list(f)
    print(list)
with open('text.txt', 'r') as f:
    list = f.readlines()
    print(list)

# write() [returns the number of characters written]
with open('text2.txt', 'w') as f:
    print('\n' + str(f.write('This is a test\n')))
    value = ('the answer', 42)
    s = str(value)
    print(f.write(s + '\n'))
print()

# f.seek [To change the file object’s position, use f.seek(offset, from_what)]
with open('workfile', 'rb+') as f:
    f.write(b'0123456789abcdef')
    print(f.seek(5))        # Go to the 6th byte in the file
    print(f.read(1))
    print(f.seek(-3, 2))     # Go to the 3rd byte before the end
    print(f.read(1))


