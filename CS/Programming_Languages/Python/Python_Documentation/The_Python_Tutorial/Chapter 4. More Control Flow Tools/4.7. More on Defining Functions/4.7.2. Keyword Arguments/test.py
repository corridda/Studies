# Functions can also be called using keyword arguments of the form kwarg=value.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!\n")

# This function can be called in any of the following ways:
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# but all the following calls would be invalid:
# parrot()                     # required argument missing
# # parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# # parrot(110, voltage=220)     # duplicate value for the same argument
# # parrot(actor='John Cleese')  # unknown keyword argument

# No argument may receive a value more than once. Here’s an example that fails due to this restriction:
def function(a):
    pass

# function(15, a = 20)


# **name receives a dictionary (must be final parameter)
# *name receives a tuple containing
#  (*name must occur before **name.)
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

