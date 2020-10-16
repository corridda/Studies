#! /usr/bin/env python3

"""Falsify a message."""
__author__ = 'Igor Vasilev'

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Alice and Bob's Shared Key
test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aesCipher = Cipher(algorithms.AES(test_key),
                   modes.ECB(),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

message_1 = b"""
FROM: FIELD AGENT ALICE
TO: FIELD AGENT BOB
RE: Meeting
DATE: 2001-1-1

Meet me today at the docks at 2300."""

message_2 = b"""
FROM: FIELD AGENT ALICE
TO: FIELD AGENT BOB
RE: Meeting
DATE: 2001-1-2

Meet me tomorrow by the store at 2200."""


message_1 += b"E" * (-len(message_1) % 16)
ciphertext_1 = aesEncryptor.update(message_1)

message_2 += b"E" * (-len(message_2) % 16)
ciphertext_2 = aesEncryptor.update(message_2)

falsified_message_ciphertext = ''.join([ciphertext_1.hex()[i:i+32] \
                                    if ciphertext_1.hex()[i:i+32] == ciphertext_2.hex()[i:i+32] \
                                else ciphertext_2.hex()[i:i+32]
                                for i in range(0, len(ciphertext_1.hex()), 32)])


print(f"plaintext_1:\n{message_1}")
print(f"ciphertext_1:\n{ciphertext_1.hex()}\n")

print(f"plaintext_2:\n{message_2}")
print(f"ciphertext_2:\n{ciphertext_2.hex()}\n")

print(f"falsified_message_ciphertext:\n{falsified_message_ciphertext}\n")

recovered_falsified_message = aesDecryptor.update(bytes.fromhex(falsified_message_ciphertext))
print(f"recovered_falsified_message:\n{recovered_falsified_message}\n")


if (message_2 == recovered_falsified_message):
    print("[PASS]")
else:
    print("[FAIL]")
