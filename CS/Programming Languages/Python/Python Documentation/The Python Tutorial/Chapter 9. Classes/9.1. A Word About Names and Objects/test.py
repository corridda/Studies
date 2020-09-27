a = 5
b = [1, 2, 3]


# 'func' doesn't change the 'obj'...
def func(obj):
    if isinstance(obj, int):
        return obj + 5
    elif isinstance(obj, list):
        return obj + [4]


print(func(a))
print('a:', a)
print(func(b))
print('b:', b)


# ... and 'func2' doesn't change the 'obj' either
def func2(obj):
    if isinstance(obj, int):
        obj + 5
    elif isinstance(obj, list):
        obj + [4]

func2(a)
print('\na:', a)
func2(b)
print('b:', b)
