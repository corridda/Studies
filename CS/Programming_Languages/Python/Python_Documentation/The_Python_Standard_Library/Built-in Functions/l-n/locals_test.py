"""locals()"""
# https://www.programiz.com/python-programming/methods/built-in/locals

"""Update and return a dictionary representing the current local symbol table.
Free variables are returned by locals() when it is called in function blocks, but not in class blocks.

Note: The contents of this dictionary should not be modified; changes may not affect the values of local
and free variables used by the interpreter.
 """

"""A symbol table is a data structure maintained by a compiler which contains all necessary information
about the program. These include variable names, methods, classes, etc.

There are mainly two kinds of symbol table.
-> Global symbol table
-> Local symbol table

A Global symbol table stores all information related to the global scope of the program, and is accessed
in python using globals() method.
The global scope contains all functions, variables which are not associated to any class or function.

Likewise, Local symbol table stores all information related to the local scope of the program,
and is accessed in python using locals() method.
The local scope could be within a function, within a class, etc. """

from pprint import pprint

# Example 1: How locals() works in python?
print(f"locals():")
pprint(locals())
print()

# Note: globals() and locals() symbol table for the global environment is the same.
print("globals():")
pprint(globals())
print()


# Example 2: How locals() works inside a local scope?
def localsNotPresent():
    return locals()

def localsPresent():
    present = True
    return locals()

print(f'localsNotPresent: {localsNotPresent()}')
print(f'localsPresent: {localsPresent()}\n')


# Example 3: Updating locals() dictionary values
"""Unlike, globals() dictionary which reflects the change to the actual global table,
locals() dictionary may not change the information inside the locals table."""

def localsPresent():
    present = True
    print(f"present: {present}")
    locals()['present'] = False
    print(f"present: {present}")
    print(locals())

localsPresent()
