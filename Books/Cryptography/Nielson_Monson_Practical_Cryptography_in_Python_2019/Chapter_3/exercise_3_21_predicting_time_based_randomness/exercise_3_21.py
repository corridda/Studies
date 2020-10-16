import os
import random
from time import time


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding



def xor_data(data_1: bytes, data_2: bytes):
    """XOR the data_1 with the data_2.

    :param data_1: bytes
    :param data_2: bytes
    """
    return bytes(pair[0] ^ pair[1] for pair in zip(data_1, data_2))


class InsecureEncryptionManager:
    def __init__(self, seed: int):
        random.seed(seed)
        self.key = random.randbytes(16)
        self.iv  = random.randbytes(16)
        aesContext = Cipher(algorithms.AES(self.key),
                            modes.CBC(self.iv),
                            backend=default_backend())
        self.encryptor = aesContext.encryptor()
        self.decryptor = aesContext.decryptor()
        self.padder = padding.PKCS7(128).padder()
        self.unpadder = padding.PKCS7(128).unpadder()

    def update_encryptor(self, plaintext):
        return self.encryptor.update(self.padder.update(plaintext))

    def finalize_encryptor(self):
        return self.encryptor.update(self.padder.finalize()) + self.encryptor.finalize()

    def update_decryptor(self, ciphertext):
        return self.unpadder.update(self.decryptor.update(ciphertext))

    def finalize_decryptor(self):
        return self.unpadder.update(self.decryptor.finalize()) + self.unpadder.finalize()


def guess_the_key(plaintext, ciphertext: bytes, min_time: int, max_time: int):
    for seed in range(min_time, max_time+1):
        manager = InsecureEncryptionManager(seed=seed)
        cur_ciphertext = manager.update_encryptor(plaintext) + manager.finalize_encryptor()
        if cur_ciphertext == ciphertext:
            return manager.key
    return None


if __name__ == '__main__':
    plaintext = b'This is a plain text.'
    cur_time = time()
    seed = int(round(cur_time, 0))
    manager = InsecureEncryptionManager(seed=seed)
    ciphertext = manager.update_encryptor(plaintext) + manager.finalize_encryptor()

    key = guess_the_key(
        plaintext=plaintext,
        ciphertext=ciphertext,
        min_time=int(round(cur_time - 10, 0)),
        max_time=int(round(cur_time + 10, 0))
    )
    if key is not None:
        print(f"Key: {ciphertext.hex()[2:]}")
    else:
        print("The key wasn't found.")
