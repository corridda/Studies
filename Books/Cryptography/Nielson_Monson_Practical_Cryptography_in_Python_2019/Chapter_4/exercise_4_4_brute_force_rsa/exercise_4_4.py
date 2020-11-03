"""Related links:
Python RSA Brute Force Check
https://stackoverflow.com/questions/28254910/python-rsa-brute-force-check
"""

# !/usr/bin/python3
__author__ = 'Igor Vasilev'

from itertools import product
from string import ascii_lowercase
from random import choices
from time import perf_counter
from contextlib import contextmanager

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


@contextmanager
def time_measurer():
    start = perf_counter()
    yield
    print(f"The elapsed time: {perf_counter() - start}\n")


def simple_rsa_encrypt(m, publickey):
    numbers = publickey.public_numbers()
    return pow(m, numbers.e, numbers.n)


def int_to_bytes(i):
    i = int(i)
    return i.to_bytes((i.bit_length() + 7) // 8, byteorder='big')


def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')


def brute_force(cyphertext: bytes, public_key, plaintext_length: int):
    perms = [''.join(s) for s in product(ascii_lowercase, repeat=plaintext_length)]
    for p in perms:
        if int_to_bytes(simple_rsa_encrypt(bytes_to_int(bytes(p, encoding='utf-8')), public_key)) == \
                cyphertext:
            return p
    return None


if __name__ == '__main__':
    messages = [
        bytes(''.join(choices(ascii_lowercase, k=3)), encoding='utf-8'),
        bytes(''.join(choices(ascii_lowercase, k=4)), encoding='utf-8'),
    ]

    # Create new public and private keys.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    for i, message in enumerate(messages, start=1):
        # Encrypt Message
        message_as_int = bytes_to_int(message)
        cipher_as_int = simple_rsa_encrypt(message_as_int, public_key)
        cipher = int_to_bytes(cipher_as_int)

        # Brute force decrypted message
        with time_measurer():
            if (plaintext := brute_force(cipher, public_key, len(message))) is None:
                print(f"Test {i}: [FAIL]")
                print(f"The message: {message}")
            else:
                print(f"Test {i}: [PASS]")
                print(f"Brute force decrypted message: {plaintext}")
