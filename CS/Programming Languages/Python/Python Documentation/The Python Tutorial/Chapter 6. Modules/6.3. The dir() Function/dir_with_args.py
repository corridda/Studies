import fibo, sys

# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:
print(dir(fibo))
print(dir(sys))

import builtins
print(dir(builtins))
