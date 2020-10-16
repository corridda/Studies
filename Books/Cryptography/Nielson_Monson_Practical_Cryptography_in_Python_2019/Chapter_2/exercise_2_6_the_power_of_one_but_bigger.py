from random import choice
from hashlib import md5
from string import ascii_letters, digits, printable
from time import perf_counter
from statistics import mean


def find_hash_match(preimage_seed: str, test_hash: str, alphabet):
    for c in alphabet:
        if md5(bytes(c, encoding='utf-8')).hexdigest() == test_hash:
            return c


if __name__ == '__main__':
    for alphabet in [ascii_letters, ascii_letters + digits, printable]:
        print(f"alphabet: {alphabet}")
        average_time = []
        for i in range(5):
            start = perf_counter()
            preimage_seed = choice(alphabet)
            test_hash = md5(bytes(preimage_seed, encoding='utf-8')).hexdigest()
            find_hash_match(preimage_seed, test_hash, alphabet)
            t = perf_counter() - start
            average_time.append(t)
        print(f"average time: {mean(average_time)}\n")


