#! usr/bin/python3

"""
1.1. The first two numbers that are both squares and triangles are 1 and 36. Find the
next one and, if possible, the one after that. Can you figure out an efficient way to find
triangular-square numbers? Do you think that there are infinitely many?

Mind also:
https://math.stackexchange.com/questions/394858/square-trangular-numbers-checking-answer
"""

__author__ = "Vasilev Igor"


from secrets import token_hex
from math import sqrt


def get_next_triangle(n: int, prev_triangle: int) -> int:
    """Get a triangle number based on given 'n'.

    :param n: an integer representing the number of elements in the bottom line
        of the triangle number (a number that can be arranged in the shape of a triangle)
    :param prev_triangle: the previous triangle number ht bottom of which is n - 1
    :returns a triangle number formed as a sum of 'n' and the previous triangle number
    """
    return prev_triangle + n

def get_next_triangle_square_pells_equation(s_k1: int, s_k0: int) -> int:
    """Get a square-triangle number based on given square roots of two previous.

    :param s_k1: an integer that is a root of the previous square-triangle number
    :param s_k0: an integer that is a root of the pre-previous square-triangle number
    :returns the next squre-triangle number formed on the basis of the one of Pell's equation solution
    """
    return (6 * s_k1 - s_k0) ** 2



def main():
    # Method 1
    print(f"Method 1")
    triangles = [sum(range(1, i + 1)) for i in range(2, 9)]
    iter_ = iter(range(9, int(token_hex(20), base=16)))

    sqr_triangles = [1, 36]
    while len(sqr_triangles) < 5:
        triangles.append(get_next_triangle(bottom := next(iter_), triangles[-1]))

        if (sq := sqrt(triangles[-1])) - int(sq) == 0:
            sqr_triangles.append(triangles[-1])
            sq = sqr_triangles[-1]
            print(f"next triangle-square: {sq}; square_bottom: {bottom}; sqrt({sq}): {sqrt(sq)}, ")

    # Method 2
    print(f"\nMethod 2")
    sqr_triangles = [1, 36]
    for _ in range(10):
        next_sq_tr = (
            get_next_triangle_square_pells_equation(
                int(sqrt(sqr_triangles[-1])), int(sqrt(sqr_triangles[-2])))
        )
        sqr_triangles.append(next_sq_tr)
    print(f"First ten square-triangle numbers:\n{sqr_triangles}")


if __name__ == '__main__':
    main()
