"""all(iterable)"""
# https://www.programiz.com/python-programming/methods/built-in/all

"""Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:"""

def all_func(iterable):
    for element in iterable:
        if not element:
            return False
    return True


def main():
    list = [1, 2, 3, 4, 5]
    empty_list = []
    list_2 = [0, 1, 2, 3]
    list_3 = [3 < 2, True]

    print(f"all_func(list): {all_func(list)}")
    print(f"all(list): {all(list)}\n")

    print(f"all_func(empty_list): {all_func(empty_list)}")
    print(f"all(empty_list): {all(empty_list)}\n")

    # 0 == False
    print(f"all_func(list_2): {all_func(list_2)}")
    print(f"all(list_2): {all(list_2)}\n")

    print(f"all_func(list_3): {all_func(list_3)}")
    print(f"all(list_3): {all(list_3)}\n")


    # How all() works for strings?
    s = "This is good"
    print(f"s: {s}")
    print(f"all(s): {all(s)}\n")

    # 0 is False
    # '0' is True
    s = '000'
    print(f"s: {s}")
    print(f"all(s): {all(s)}\n")

    s = ''
    print(f"s: {s}")
    print(f"all(s): {all(s)}\n")


    # How all() works with Python dictionaries?
    """In case of dictionaries, if all keys (not values) are true or the dictionary is empty,
    all() returns True. Else, it returns false for all other cases.."""
    d = {0: 'False', 1: 'False'}
    print(f"d: {d}")
    print(f"all(d): {all(d)}\n")

    d = {1: 'True', 2: 'True'}
    print(f"d: {d}")
    print(f"all(d): {all(d)}\n")

    d = {1: 'True', False: 0}
    print(f"d: {d}")
    print(f"all(d): {all(d)}\n")

    d = {}
    print(f"d: {d}")
    print(f"all(d): {all(d)}\n")

    # 0 is False
    # '0' is True
    d = {'0': 'True'}
    print(f"d: {d}")
    print(f"all(d): {all(d)}\n")


if __name__ == "__main__":
    main()
