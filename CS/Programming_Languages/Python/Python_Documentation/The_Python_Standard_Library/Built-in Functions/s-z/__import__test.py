"""__import__(name, globals=None, locals=None, fromlist=(), level=0)"""
# https://www.programiz.com/python-programming/methods/built-in/__import__

"""Note:
 This is an advanced function that is not needed in everyday python programming, unlike importlib.import_module().
 It is rarely used and often discouraged.
 The function imports the module name, potentially using the given globals and locals to determine
 how to interpret the name in a package context. The fromlist gives the names of objects or submodules
 that should be imported from the module given by name. The standard implementation does not use
 its locals argument at all, and uses its globals only to determine the package context of the import statement.

level specifies whether to use absolute or relative imports. 0 (the default) means only perform absolute imports.
Positive values for level indicate the number of parent directories to search relative to the directory
of the module calling __import__() (see PEP 328 for the details).

When the name variable is of the form package.module, normally, the top-level package (the name up till the first dot)
is returned, not the module named by name. However, when a non-empty fromlist argument is given,
the module named by name is returned.

If you simply want to import a module (potentially within a package) by name, use importlib.import_module().
"""

# Example: How __import()__ works?

mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))

"""In general, fabs() is a method defined in math module. You can call this function using the following syntax:
    math.fabs(x)
However, using __import__() changed the way to access fabs() in the above program.
"""
