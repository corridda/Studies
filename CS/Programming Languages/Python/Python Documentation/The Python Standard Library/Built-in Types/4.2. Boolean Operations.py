"""Boolean Operations — and, or, not"""

"""x or y:
    if x is false, then y, else x
This is a short-circuit operator, so it only evaluates the second argument if the first one is false."""

x = False
y = True
if x or y:
    print(f"'y' was evaluated.")


"""x and y:
    if x is false, then x, else y
This is a short-circuit operator, so it only evaluates the second argument if the first one is true."""

x = True
y = True
if x and y:
    print(f"'y' was evaluated.")


"""not x
    if x is false, then True, else False
'not' has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b),
and a == not b is a syntax error"""

x = True
if not x:
    print(f"'x' is True")
else:
    print(f"'x' is False")