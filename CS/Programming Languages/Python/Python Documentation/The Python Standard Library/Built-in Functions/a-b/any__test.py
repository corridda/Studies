"""any(iterable)"""
# https://www.programiz.com/python-programming/methods/built-in/any

"""Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:"""

def any_func(iterable):
    for element in iterable:
        if element:
            return True
    return False


def main():
    list = [1, 2, 3, 4, 5]
    empty_list = []
    list_2 = [0, 1, 2, 3]
    list_3 = [3 < 2, False]

    print(f"any_func(list): {any_func(list)}")
    print(f"any(list): {any(list)}\n")

    print(f"any_func(empty_list): {any_func(empty_list)}")
    print(f"any(empty_list): {any(empty_list)}\n")

    print(f"any_func(list_2): {any_func(list_2)}")
    print(f"any(list_2): {any(list_2)}\n")

    print(f"any_func(list_3): {any_func(list_3)}")
    print(f"any(list_3): {any(list_3)}\n")


    # How any() works with Python Strings?
    s = "This is good"
    print(f"s: {s}")
    print(f"any(s): {any(s)}\n")

    # 0 is False
    # '0' is True
    s = '000'
    print(f"s: {s}")
    print(f"any(s): {any(s)}\n")

    s = ''
    print(f"s: {s}")
    print(f"any(s): {any(s)}\n")


    # How any() works with Python Dictionaries?
    """In case of dictionaries, if all keys (not values) are false, any() returns False.
    If at least one key is true, any() returns True."""
    d = {0: 'False'}
    print(f"d: {d}")
    print(f"any(d): {any(d)}\n")

    d = {0: 'False', 1: 'True'}
    print(f"d: {d}")
    print(f"any(d): {any(d)}\n")

    d = {0: 'False', False: 0}
    print(f"d: {d}")
    print(f"any(d): {any(d)}\n")

    d = {}
    print(f"d: {d}")
    print(f"any(d): {any(d)}\n")

    # 0 is False
    # '0' is True
    d = {'0': 'False'}
    print(f"d: {d}")
    print(f"any(d): {any(d)}\n")


if __name__ == "__main__":
    main()
