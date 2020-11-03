import math
from math import factorial, prod, sqrt
from decimal import Decimal
from time import perf_counter


def combinations_factor(n, k, repetitions=False):
    """Compute the number of combinations using factorials.
    :param n: the size of initial set of elements to choose from
    :param k: the number of elements to choose from initial set
    :return: the number of combinations
    """
    if repetitions:
        n = n + k - 1
    return Decimal(Decimal(factorial(n)) / Decimal((factorial(n - k) * factorial(k))))


def combinations_products(n, k, repetitions=False):
    """Compute the number of combinations more efficiently than using factorials.
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


def combinations_Strirlings_Approximation(n, k, repetitions=False):
    """Compute the number of combinations using Stirling’s approximation.
    :param n: the size of initial set of elements to choose from
    :param k: the number of elements to choose from initial set
    :return: the number of combinations
    """
    if repetitions:
        n = n + k - 1

    def stirling_approx(num):
        return Decimal(sqrt(2 * math.pi * num)) * Decimal(num / math.pi)**num

    return Decimal(stirling_approx(n) / (stirling_approx(n - k) * stirling_approx(k))).to_integral_value()


if __name__ == '__main__':
    n = 15000
    k = 1200

    print(f"n: {n}\nk: {k}\n")

    t0 = perf_counter()
    res1 = combinations_factor(n=n, k=k, repetitions=False)
    print(f"combinations_factor, sec: {perf_counter() - t0}")
    print(f"combinations number: {res1}\n")

    t0 = perf_counter()
    res2 = combinations_products(n=n, k=k, repetitions=False)
    print(f"combinations_products, sec: {perf_counter() - t0}")
    print(f"combinations number: {res2}")
    print(f"res2 - res1 = {res2 - res1}\n")

    t0 = perf_counter()
    res3 = combinations_Strirlings_Approximation(n=n, k=k, repetitions=False)
    print(f"combinations_Strirlings_Approximation, sec: {perf_counter() - t0}")
    print(f"combinations number: {res3}")
    print(f"res3 - res2 = {res3 - res2}")
