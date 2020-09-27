import test_module

print(f'test_module.a: {test_module.a}')

# del
del test_module.a
try:
    print(test_module.a)
except AttributeError as e:
    print(repr(e))

# module namespaces last until the interpreter quits
test_module.a = 43
print(f'test_module.a: {test_module.a}')


# The global scope of a function defined in a module is that module’s namespace,
# no matter from where or by what alias the function is called.

# global variable 'a'
a = 1

# but test_module has its own 'a', though it prints its own 'a'
test_module.print_a()
