# !/usr/bin/python3
__author__ = 'Igor Vasilev'

from itertools import product
from string import ascii_lowercase
from random import choices
from time import perf_counter

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa



def simple_rsa_encrypt(m, publickey):
    numbers = publickey.public_numbers()
    return pow(m, numbers.e, numbers.n)


def int_to_bytes(i):
    i = int(i)
    return i.to_bytes((i.bit_length() + 7) // 8, byteorder='big')


def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')


def brute_force_worst_case(cyphertext: bytes, public_key, plaintext_length: int):
    perms = [''.join(s) for s in product(ascii_lowercase, repeat=plaintext_length)]
    for p in perms:
        int_to_bytes(simple_rsa_encrypt(bytes_to_int(bytes(p, encoding='utf-8')), public_key))



if __name__ == '__main__':
    messages = [
        bytes(''.join(choices(ascii_lowercase, k=3)), encoding='utf-8'),
        bytes(''.join(choices(ascii_lowercase, k=4)), encoding='utf-8'),
        bytes(''.join(choices(ascii_lowercase, k=5)), encoding='utf-8'),
    ]

    # Create new public and private keys.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    for i, message in enumerate(messages, start=3):
        # Encrypt Message
        message_as_int = bytes_to_int(message)
        cipher_as_int = simple_rsa_encrypt(message_as_int, public_key)
        cipher = int_to_bytes(cipher_as_int)

        # Brute force decrypted message
        start = perf_counter()
        brute_force_worst_case(cipher, public_key, len(message))
        time_ = perf_counter() - start
        print(f"Time to brute force a {i}-letter word (worst case): {round(time_, 2)} sec.")


# >>> Time to brute force a 3-letter word (worst case): 2.04 sec.
# >>> Time to brute force a 4-letter word (worst case): 53.45 sec.
# >>> Time to brute force a 5-letter word (worst case): 1436.22 sec.
