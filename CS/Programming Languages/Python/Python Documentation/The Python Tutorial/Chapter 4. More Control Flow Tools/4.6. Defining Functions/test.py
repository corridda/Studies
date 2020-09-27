# We can create a function that writes the Fibonacci series to an arbitrary boundary:
def fib(x):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while True:
        if a < x:
            print(a, '', end='')
        else:
            break
        a, b = b, a + b

print(fib.__doc__)
fib(2000)
print()

# renaming mechanism
print(fib)
f = fib
f(100)
print()
print(f(100))
print()

# It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:
def fib2(x):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while True:
        if a < x:
            result.append(a)
        else:
            break
        a, b = b, a + b
    return result

print(fib2(100))

def return_None():
    return

print(return_None())