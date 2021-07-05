"""That XOR Trick
https://florian.github.io/xor-trick/
"""

from secrets import token_hex
from itertools import permutations

def xor_commutativity(hex_strigs: list[str]) -> bool:
    """Practical prove of XOR commutativity.

    :param hex_strigs: a list of hex strings
    :return: whether or not all XORs of all elements of each one of hex_strings permutations are equal.
    """
    perms = [p for p in permutations(hex_strings, 4)]
    all_xors = []
    for p in perms:
        temp = int(p[0], base=16)
        for hex_s in p[1:]:
            temp ^= int(hex_s, base=16)
        all_xors.append(temp)
    return all([x == all_xors[0] for x in all_xors])


if __name__ == '__main__':
    # get some hex strings
    hex_strings = [token_hex(16) for  _ in range(4)]

    print(f"XOR is a commutative math operation: {xor_commutativity(hex_strings)}")