from math import prod
from decimal import Decimal


def permutations(n, k, repetitions=False):
    """Compute the number of k-permutations of n.
    :param n: the size of initial set of elements to choose from
    :param k: the number of elements to choose from initial set
    :return: the number of permutations
    """
    if repetitions:
        return Decimal(n**k).to_integral_value()
    return Decimal(prod(range(n-k+1, n+1))).to_integral_value()


def combinations(n, k, repetitions=False):
    """Compute the number of combinations.
    :param n: the size of initial set of elements to choose from
    :param k: the number of elements to choose from initial set
    :return: the number of combinations
    """
    if repetitions:
        n = n + k - 1
    numerator = set(range(n - k + 1, n + 1))
    denominator = set(range(1, k + 1))
    num = numerator.difference(denominator)
    denom = denominator.difference(numerator)
    return Decimal(Decimal(prod(num)) / Decimal(prod(denom))).to_integral_value()


if __name__ == '__main__':
    n = 10
    k = 5
    print(f"permutations({n}, {k}): {permutations(n, k, repetitions=True):}")
