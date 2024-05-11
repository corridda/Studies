"""(b) Find a list of 100 consecutive composite integers."""

from books.auxiliary import is_prime


def main():
    prev_prime = 2
    next_prime = 3

    while next_prime - prev_prime < 101:
        prev_prime = next_prime
        next_prime_candidate = prev_prime + 2
        while not is_prime(next_prime_candidate):
            next_prime_candidate += 2
        next_prime = next_prime_candidate

    conseq_composite_nums = [i for i in range(prev_prime + 1, next_prime)]
    print(f"Found primes: {prev_prime}, {next_prime}\n"
          f"Consecutive numbers: {conseq_composite_nums[:100]}\n"
          f"len(conseq_composite_nums[:100]): {len(conseq_composite_nums[:100])}")


if __name__ == '__main__':
    main()
