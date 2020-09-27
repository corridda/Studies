def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok("Do you really want to quit?: ")
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# It will print 5
i = 5
def print_i(arg = i):
    print(arg)

i = 6
print_i()

# but this will print 6
print_i(i)
print()

"""
Important warning: The default value is evaluated only once.
This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes
"""
def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print()

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a, L = None):
    if L == None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
