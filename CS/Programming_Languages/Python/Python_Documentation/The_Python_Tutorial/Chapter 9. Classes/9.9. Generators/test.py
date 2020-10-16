# this is a trivial generator
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
print()


# another solution of the same problem
for i in range(len('golf')-1, -1, -1):
    print('golf'[i])