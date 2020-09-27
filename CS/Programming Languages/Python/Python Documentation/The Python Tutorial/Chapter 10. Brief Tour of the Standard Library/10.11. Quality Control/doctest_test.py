# The doctest module provides a tool for scanning a module and validating tests embedded in a program’s docstrings.

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

# automatically validate the embedded tests
print(doctest.testmod())

print('average(20,30,70):', average([20,30,70]))