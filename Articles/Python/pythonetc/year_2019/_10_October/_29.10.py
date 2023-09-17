"""https://t.me/pythonetc/502"""

"""In python 3, once the except block is exited, the variables that store caught exceptions are removed
from locals() even if they previously existed:"""

e = 2
try:
    1/0
except Exception as e:
    pass

try:
    print(e)
except NameError as nameEr:
    print(repr(nameEr))


"""If you want to save a reference to the exception, you have to use another variable:"""
error = None
try:
    1/0
except Exception as e:
    error = e
print(f"error: {error}")
