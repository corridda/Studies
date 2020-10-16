import sys

# sys.ps1 and sys.ps2
# These two variables are only defined if the interpreter is in interactive mode.
# it leads to an error
# print(sys.ps1)


# The variable sys.path is a list of strings that determines the interpreter’s search path for modules.
for i in sys.path:
    print(i)