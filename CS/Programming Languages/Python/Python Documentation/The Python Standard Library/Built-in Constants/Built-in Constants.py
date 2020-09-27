"""Built-in Constants"""



"""False, True, None"""
# Assignments to False, True, None are illegal and raise a SyntaxError.
print(False, True, None)
print(type(False), type(True), type(None), '\n')



"""NotImplemented"""
"""Special value which should be returned by the binary special methods (e.g. __eq__(), __lt__(), __add__(),
__rsub__(), etc.) to indicate that the operation is not implemented with respect to the other type;
may be returned by the in-place binary special methods (e.g. __imul__(), __iand__(), etc.) for the same purpose.
Its truth value is true."""

class A:
    pass

print(int.__eq__(10, A()))



"""Constants added by the site module"""

"""The site module (which is imported automatically during startup, except if the -S command-line option is given)
adds several constants to the built-in namespace. They are useful for the interactive interpreter shell
and should not be used in programs.
    quit(code=None)
    exit(code=None)
Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”, and when called,
raise SystemExit with the specified exit code.
    copyright
    credits
Objects that when printed or called, print the text of copyright or credits, respectively.
    license
Object that when printed, prints the message “Type license() to see the full license text”, and when called,
displays the full license text in a pager-like fashion (one screen at a time).
"""

