"""
The global statement can be used to indicate that particular variables live in the global scope
and should be rebound there;
the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.
"""

# 'a' is global
a = 42


def func():
    b = 100
    print('b =', b)

    # this 'a' is local
    a = 43
    print('local "a" =', a)

    def func_inside():
        nonlocal a
        a = 'nonlocal "a"'

    a = 'test "a"'
    # 'func_inside()' changes 'a' which is living in an enclosing scope
    func_inside()
    print('"a" =', a)


def func2():
    global a

    # you have an access to global 'a' from here
    print('global "a" accessible inside the "func" =', a)


print('a =', a)
func2()
func()

# 'b' is local for func, so it's not accessible here
# print('b =', b)
