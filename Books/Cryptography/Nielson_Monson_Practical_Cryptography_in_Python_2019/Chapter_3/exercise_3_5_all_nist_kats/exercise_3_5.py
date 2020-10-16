#! /usr/bin/env python3

"""KAT's (known answer tests)"""
__author__ = 'Igor Vasilev'


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def make_test(test, key, plaintext_bytes, ciphertext, encrypt: True):
    """Make a single test.

    :param test: a test number
    :param key: a key (bytes)
    :param plaintext_bytes: a plain text (bytes)
    :param ciphertext: a ciphertext
    """
    aesCipher = Cipher(algorithms.AES(key),
                       modes.ECB(),
                       backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    aesDecryptor = aesCipher.decryptor()
    if encrypt:
        ciphertext_bytes = aesEncryptor.update(plaintext_bytes)
        got_ciphertext = ciphertext_bytes.hex()
        result = "[PASS]" if got_ciphertext == ciphertext else "[FAIL]"
        print(f"Test {test}. Expected {ciphertext}, got {got_ciphertext}. Result {result}.")
    else:
        got_plaintext_bytes = aesDecryptor.update(bytes.fromhex(ciphertext))
        got_plaintext = got_plaintext_bytes.hex()
        result = "[PASS]" if got_plaintext == plaintext_bytes.hex() else "[FAIL]"
        print(f"Test {test}. Expected {plaintext_bytes.hex()}, got {got_plaintext}. Result {result}.")


def make_tests(path: str):
    """Make all KAT's from the file by the given path.

    :param path: the path to the file with KAT's
    """
    with open(path, 'r') as f:
        lines = iter(f.readlines())
        try:
            test, key, plaintext_bytes, ciphertext = None, None, None, None
            print(f"ENCRIPTION TESTS:")
            while (cur_line := next(lines).strip()) != '[DECRYPT]':
                if cur_line.startswith('COUNT'):
                    test = cur_line.strip().split()[-1]
                if cur_line.startswith('KEY'):
                    key = bytes.fromhex(cur_line.strip().split()[-1])
                elif cur_line.startswith('PLAINTEXT'):
                    plaintext_bytes = bytes.fromhex(cur_line.strip().split()[-1])
                elif cur_line.startswith('CIPHERTEXT'):
                    ciphertext = cur_line.strip().split()[-1]

                if test is not None \
                        and key is not None \
                        and plaintext_bytes is not None \
                        and ciphertext is not None:
                    make_test(test, key, plaintext_bytes, ciphertext, encrypt=True)
                    test, key, plaintext_bytes, ciphertext = None, None, None, None

            print(f"\n\nDECRIPTION TESTS:")
            while cur_line := next(lines):
                if cur_line.startswith('COUNT'):
                    test = cur_line.strip().split()[-1]
                if cur_line.startswith('KEY'):
                    key = bytes.fromhex(cur_line.strip().split()[-1])
                elif cur_line.startswith('PLAINTEXT'):
                    plaintext_bytes = bytes.fromhex(cur_line.strip().split()[-1])
                elif cur_line.startswith('CIPHERTEXT'):
                    ciphertext = cur_line.strip().split()[-1]

                if test is not None \
                        and key is not None \
                        and plaintext_bytes is not None \
                        and ciphertext is not None:
                    make_test(test, key, plaintext_bytes, ciphertext, encrypt=False)
                    test, key, plaintext_bytes, ciphertext = None, None, None, None

        except StopIteration:
            pass


if __name__ == '__main__':
    make_tests('./input/ECBVarKey256.rsp')
