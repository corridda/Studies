"""exec(object[, globals[, locals]])"""
# https://www.programiz.com/python-programming/methods/built-in/exec

"""
    Execute the given source in the context of globals and locals.
    
    The source may be a string representing one or more python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
"""

from math import *

def main():
    """The exec() doesn't return any value, it returns None.
    Hence, you cannot use return and yield statements outside of the function definitions."""
    program = 'a = 5\nb=10\nprint(f"{a} + {b} = {a + b}")'
    exec(program)

    # Allow user to provide input
    # program = input('Enter a program:') # a = 5; b = 10; print(f"{a} * {b} = {a*b}")
    # exec(program)

    """Warning!
    If you allow users to input a value using exec(input()), the user may issue commands to change file
    or even delete all the files using command os.system('rm -rf *')."""

    """If you are using exec(input()) in your code, it's a good idea to check which variables
    and methods the user can use. You can see which variables and methods are available using dir() method."""
    exec('print(dir())')

    # In other cases exec() behaves like eval().

if __name__ == "__main__":
    main()
