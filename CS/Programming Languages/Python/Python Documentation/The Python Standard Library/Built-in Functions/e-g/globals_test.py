"""globals()"""
# https://www.programiz.com/python-programming/methods/built-in/globals

"""Return a dictionary representing the current global symbol table.
This is always the dictionary of the current module """

def func():
    a, b = 10, 20
    print(f"locals(): {locals()}\n")
func()

try:
    for k, v in globals().items():
        print(k + ': ' + v)
except RuntimeError as e:
    print(print(repr(e)))

print(f"\nglobals():\n{globals()}\n")


# Modify global variable using global()
age = 23
globals()['age'] = 25
print('The age is:', age)
