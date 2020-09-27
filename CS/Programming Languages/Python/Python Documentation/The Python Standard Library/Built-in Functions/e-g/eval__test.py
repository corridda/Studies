"""eval(expression, globals=None, locals=None)"""
# https://www.programiz.com/python-programming/methods/built-in/eval

"""
    Evaluate the given source in the context of globals and locals.
    
    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
"""

from math import *

# Perimeter of Square
def calculatePerimeter(side: float):
    return 4 * side

# Area of Square
def calculateArea(side: float):
  return side * side


def main():
    x = 1

    # The eval() method returns the result evaluated from the expression.
    print(f"eval('x + 1'): {eval('x + 1')}")
    print(f"globals(): {globals()}")
    print(f"locals(): {locals()}\n")

    # property = input("Type a function: ")
    #
    # for side in range(1, 5):
    #     if (property == 'calculatePerimeter(side)'):
    #         print("If length is ", side, ", Perimeter = ", eval(property))
    #     elif (property == 'calculateArea(side)'):
    #         print("If length is ", side, ", Area = ", eval(property))
    #     else:
    #         print('Wrong Function')
    #         break

    # When both globals and locals parameters omitted
    """If both parameters are omitted (as in our earlier examples), the expression is executed in the current scope.
    You can check the available variables and methods using following code:"""
    print(f"eval('dir()'): {eval('dir()')}")


    # Passing globals parameter; locals parameter is omitted
    print(eval('dir()', {}))

    """If you pass an empty dictionary as globals, only the __builtins__ are available to expression
    (first parameter to the eval()). Even though we have imported math module in the above program,
    expression can't access none of the functions provided by the math module."""
    # The code below will raise an exception
    try:
        print(eval('sqrt(25)', {}))
    except NameError as e:
        print(repr(e) + '\n')

    # Making Certain Methods available
    # Here, the expression can also use sqrt() and pow() methods along with __builtins__.
    print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))

    # Also, it's possible to change the name of the method available for the expression according to your wish.
    print(eval('dir()', {'squareRoot': sqrt, 'pow': pow}))

    # Using squareRoot in Expression
    print(eval('squareRoot(9)', {'squareRoot': sqrt, 'pow': pow}), '\n')

    # You can restrict the use of __builtins__ in the expression as follows:
    # eval(expression, {'__builtins__': None})


    # Passing both globals and locals dictionary
    """You can make needed functions and variables available for use by passing locals dictionary. For example:"""
    a = 5
    print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))

    """In this program, the expression (first parameter to the eval) can have sqrt() method and variable a only.
    All other methods and variables are unavailable."""


    """Restricting the use of eval() by passing globals and locals dictionary will make your code secure
    particularly when you are using input provided by the user to the eval() method."""

if __name__ == "__main__":
    main()
