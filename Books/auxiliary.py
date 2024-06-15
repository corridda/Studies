# ! /usr/bin/env python39

"""Different useful functions"""

__author__ = 'Igor Vasilev'


def is_prime(n: int) -> bool:
    """Check whether the number 'n' is prime.

    :param n: a number to check
    :returns True if the number is prime, False otherwise
    """
    match n:
        case 1:
            return False
        case 2:
            return True
        case x if not x % 2:
            return False
        case _:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if not n % i:
                    return False
    return True


def get_next_prime(prev: int):
    """Get the next prime number that follows immediately after the given one.

    :param prev: the previous prime number
    :returns: next prime number
    """
    match prev:
        case 2:
            return 3
        case _:
            next_prime_candidate = prev + 2
            while not is_prime(next_prime_candidate):
                next_prime_candidate += 2
            return next_prime_candidate
