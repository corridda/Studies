"""enumerate(iterable, start=0)"""
# https://www.programiz.com/python-programming/methods/built-in/enumerate

"""Return an enumerate object. 'iterable' must be a sequence, an iterator,
or some other object which supports iteration."""


def main():
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(f"enumerate(seasons): {enumerate(seasons)}")
    print(f"list(enumerate(seasons)): {list(enumerate(seasons))}")
    print(f"list(enumerate(seasons, start=1)): {list(enumerate(seasons, start=1))}\n")
    print(f"dict(enumerate(seasons)): {dict(enumerate(seasons))}\n")

    # Looping Over an Enumerate object
    grocery = ['bread', 'milk', 'butter']

    for item in enumerate(grocery):
        print(item)
    print('\n')

    for count, item in enumerate(grocery):
        print(count, item)
    print('\n')

    # changing default start value
    for count, item in enumerate(grocery, start=100):
        print(count, item)


if __name__ == "__main__":
    main()