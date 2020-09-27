"""help([object])"""
# https://www.programiz.com/python-programming/methods/built-in/help

"""Invoke the built-in help system. (This function is intended for interactive use.)"""

from math import *

print(f"{help(list)}\n")
print(f"help([1, 2, 3]): {help([1, 2, 3])}\n")

"""If string is passed as an argument, name of a module, function, class, method, keyword,
or documentation topic, and a help page is printed."""
print(f"help('random thing'): {help('random thing')}\n")
print(f"help('def'): {help('def')}\n")
print(f"help('math.pow'): {help('math.pow')}\n")

# If no argument is passed, Python's help utility (interactive help system) starts on the console.
# To quit the help utility and return to the interpreter, you need to type quit and press enter.
help()
