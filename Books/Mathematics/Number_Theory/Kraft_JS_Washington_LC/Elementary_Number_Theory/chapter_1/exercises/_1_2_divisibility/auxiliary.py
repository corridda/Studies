"""Some common functions"""


def get_all_positive_divisors(n: int) -> list[int]:
    """Find all possible divisors of 'n'"""
    return [i for i in range(1, n // 2 + 1) if not n % i] + [n]
