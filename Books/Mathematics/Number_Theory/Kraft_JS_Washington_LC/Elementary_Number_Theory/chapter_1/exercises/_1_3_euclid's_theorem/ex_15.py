"""Consider the numbers
2 + 1; 2 · 3 + 1; 2 · 3 · 5 + 1; 2 · 3 · 5 · 7 + 1; · · · :
Show, by computing several values, that there are composite
numbers in this sequence. (This shows that in the proof of
Euclid’s theorem, these numbers are not necessarily prime, so
it is necessary to look at prime factors of these numbers.)
"""

from math import prod

from books.auxiliary import is_prime, get_next_prime


def main():
    list_primes = [2, 3]
    for _ in range(18):
        list_primes.append(get_next_prime(list_primes[-1]))

    composites = 0
    prime_nums_quantity = 1
    while composites < 3:
        if not is_prime(res := (prod(list_primes[:prime_nums_quantity]) + 1)):
            composites += 1
            print(f"{'·'.join([str(n) for n in list_primes[:prime_nums_quantity]])} + 1 = {res:_} -> composite")
        prime_nums_quantity += 1


if __name__ == '__main__':
    main()
