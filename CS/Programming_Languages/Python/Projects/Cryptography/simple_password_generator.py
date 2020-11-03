"""Generate a relatively secure password."""

# !/usr/bin/python3.9
__author__ = 'Igor Vasilev'

from math import ceil
from random import choices, sample
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import sys


def get_password(length: int) -> str:
    """Generate a secure password consisting from ascii letters, digits and punctuation characters.

    :param length: the desired length of a password
    """
    if length < 8:
        raise ValueError('The number of signs must be at least 6 characters.')
    len_lowercase_letters = ceil(length * 0.4)
    len_uppercase_letters = ceil(length * 0.2)
    len_digits = ceil(length * 0.3)
    len_puncts = ceil(length * 0.1)
    while sum([len_lowercase_letters, len_uppercase_letters, len_digits, len_puncts]) > length:
        len_lowercase_letters -= 1
    lower_letters = choices(ascii_lowercase, k=len_lowercase_letters)
    upper_letters = choices(ascii_uppercase, k=len_uppercase_letters)
    digits_ = choices(digits, k=len_digits)
    puncts = choices(punctuation, k=len_puncts)

    return ''.join(sample(lower_letters + upper_letters + digits_ + puncts, k=length))


if __name__ == '__main__':
    while True:
        try:
            input_ = input(f"\nEnter the number of signs (not less than 8) "
                           f"in a password to generate or 'e' to exit: ")
            if input_ in ['e', 'exit']:
                sys.exit(0)
            input_2, temp = None, None
            while True:
                if input_2 is not None and isinstance(input_2, int):
                    print(get_password(int(temp)))
                else:
                    if temp is not None:
                        print(get_password(int(temp)))
                    else:
                        print(get_password(int(input_)))
                input_2 = input("One more password? (y[es] or n[o] or the signs number)\n")
                if input_2 in ['n', 'no', 0]:
                    sys.exit(0)
                else:
                    try:
                        input_2 = int(input_2)
                        temp = input_2
                    except ValueError as e:
                        pass
        except ValueError as e:
            print(f"{repr(e)}\nWanna try again?\n")
