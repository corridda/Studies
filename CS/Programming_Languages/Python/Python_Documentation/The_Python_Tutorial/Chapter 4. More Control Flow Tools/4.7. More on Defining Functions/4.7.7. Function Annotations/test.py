def make_square(n: int) -> int:
    """Возвращает квадрат аргумента

    :param n: int
    :return: int
    """
    return n ** 2


# print(make_square(int(input('Enter the number:\n'))))
print(make_square.__annotations__)
print(make_square.__doc__)


def func(num: int, exclam: str, *arguments: str, **map: dict) -> None:
    print(exclam * num, '\n\nList of args:')
    for arg in arguments:
        print(arg)
    print('\nDictionary:')
    keys = sorted(map.keys())
    for i in keys:
        print(i, map[i], sep= ' - ')

print(func.__annotations__, '\n')

func(3, 'Whatever! ', 'Mars', 'Venus', 'Earth', two = 2, three = 3, one = 1)




