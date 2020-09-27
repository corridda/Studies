"""class dict"""
# https://www.programiz.com/python-programming/methods/built-in/dict


""" 
    class dict(**kwarg)
    class dict(mapping, **kwarg)
    class dict(iterable, **kwarg)
Create a new dictionary. The dict object is the dictionary class. See dict
and Mapping Types — dict for documentation about this class.
"""


def main():
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})

    print(f"a == b == c == d == e: {a == b == c == d == e}")


if __name__ == "__main__":
    main()
