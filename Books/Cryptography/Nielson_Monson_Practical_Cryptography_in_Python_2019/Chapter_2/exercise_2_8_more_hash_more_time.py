from random import choices
import hashlib
from string import ascii_letters, digits, printable
from time import perf_counter


def generate(alphabet, max_len):
    """The max length of 'max_len' permutations generator.

    :param alphabet: the using alphabet to make permutations
    :param max_len: the maximum length of generating permutations
    """
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len - 1):
            yield c + next


class NotAppropriateAlgorithm(Exception):
    def __init__(self):
        super().__init__('Not appropriate hash algorithm!')


def find_hash_match(preimage_seed: str, alphabet, algo: str):
    """Find the hash matching of the hash of the preimage_seed by brute-force attack.

    :param preimage_seed: a randomly selected from the alphabet sequence
    :param alphabet: the alphabet to generate permutations
    :param algo: an algorithm to compute the hashes
    """
    # Check if algorithm is available
    if algo not in hashlib.algorithms_available:
        raise NotAppropriateAlgorithm

    if algo == 'md5':
        test_hash = hashlib.md5(bytes(preimage_seed, encoding='utf-8')).hexdigest()
        gen = generate(alphabet, max_len=len(preimage_seed))
        while True:
            c = next(gen)
            if hashlib.md5(bytes(c, encoding='utf-8')).hexdigest() == test_hash:
                return
    elif algo == 'sha1':
        test_hash = hashlib.sha1(bytes(preimage_seed, encoding='utf-8')).hexdigest()
        gen = generate(alphabet, max_len=len(preimage_seed))
        while True:
            c = next(gen)
            if hashlib.sha1(bytes(c, encoding='utf-8')).hexdigest() == test_hash:
                return
    elif algo == 'sha256':
        test_hash = hashlib.sha256(bytes(preimage_seed, encoding='utf-8')).hexdigest()
        gen = generate(alphabet, max_len=len(preimage_seed))
        while True:
            c = next(gen)
            if hashlib.sha256(bytes(c, encoding='utf-8')).hexdigest() == test_hash:
                return
    else:
        raise NotAppropriateAlgorithm


if __name__ == '__main__':
    for alphabet in [ascii_letters, ascii_letters + digits, printable]:
        print(f"alphabet: {alphabet}\n")
        for k in range(2, 4):
            for algo in ['md5', 'sha1', 'sha256']:
                start = perf_counter()
                preimage_seed = ''.join(choices(alphabet, k=k))
                print(f"algo: {algo}")
                print(f"preimage_seed: {preimage_seed}")
                find_hash_match(preimage_seed, alphabet, algo)
                t = perf_counter() - start
                print(f"run time: {t}\n")
            print()
