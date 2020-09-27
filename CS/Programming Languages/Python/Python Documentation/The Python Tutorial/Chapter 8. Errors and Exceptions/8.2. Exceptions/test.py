# ZeroDivisionError: division by zero
try:
    print(10 * (1 / 0))
except ZeroDivisionError as e:
    print(e)

# NameError: name 'spam' is not defined
try:
    print(spam * 3)
except NameError as e:
    print(e)

# TypeError: Can't convert 'int' object to str implicitly
try:
    print('2' + 2)
except TypeError as e:
    print(e)
