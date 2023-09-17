"""https://t.me/pythonetc/235"""

"""In python, you can create a callable object not only by creating functions (with def or lambda).
An object is also callable if it has the __call__ magic method:"""

class truncater:
    def __init__(self, length):
        self._length = length

    def __call__(self, s):
        return s[0:self._length]


print(truncater(4)('abcdabcd')) # abcd

"""Since a decorator is basically a higher-order function, it can also be expressed
with a callable object instead of a function:"""

class cached:
    def __init__(self, func):
        self._func = func
        self._cache = {}

    def __call__(self, arg):
        if arg not in self._cache:
            self._cache[arg] = self._func(arg)

        return self._cache[arg]

@cached
def sqr(x):
    return x * x

print(f"sqr(5): {sqr(5)}")
s = cached(sqr)
print(s._cache)
