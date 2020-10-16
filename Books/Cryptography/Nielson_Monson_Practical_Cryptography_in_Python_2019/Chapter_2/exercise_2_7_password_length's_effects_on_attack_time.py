from random import choices
from hashlib import md5
from string import ascii_letters, digits, printable
from time import perf_counter


def generate(alphabet, max_len):
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len - 1):
            yield c + next


def find_hash_match(preimage_seed: str, test_hash: str, alphabet):
    gen = generate(alphabet, max_len=len(preimage_seed))
    while True:
        c = next(gen)
        if md5(bytes(c, encoding='utf-8')).hexdigest() == test_hash:
            return c


if __name__ == '__main__':
    for alphabet in [ascii_letters, ascii_letters + digits, printable]:
        print(f"alphabet: {alphabet}")
        for k in range(2, 5):
            start = perf_counter()
            preimage_seed = ''.join(choices(alphabet, k=k))
            print(f"preimage_seed: {preimage_seed}")
            test_hash = md5(bytes(preimage_seed, encoding='utf-8')).hexdigest()
            find_hash_match(preimage_seed, test_hash, alphabet)
            t = perf_counter() - start
            print(f"k: {k}")
            print(f"time: {t}\n")
        print()
