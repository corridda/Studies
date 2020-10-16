import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding



def xor_data(data_1: bytes, data_2: bytes):
    """XOR the data_1 with the data_2.

    :param data_1: bytes
    :param data_2: bytes
    """
    return bytes(pair[0] ^ pair[1] for pair in zip(data_1, data_2))


class EncryptionManager:
    def __init__(self, key, iv):
        self.key = key
        self.iv  = iv
        aesContext = Cipher(algorithms.AES(self.key),
                            modes.CTR(self.iv),
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


def get_keastream(plaintext: bytes, ciphertext: bytes) -> bytes:
    """Get the keystream by XORing the plaintext and the ciphertext"""
    return bytes(pair[0] ^ pair[1] for pair in zip(plaintext, ciphertext))


if __name__ == '__main__':
    # Key and IV mustn't be the same!
    key = os.urandom(16)
    iv = os.urandom(16)

    with open('message_1.txt', 'rb') as m1:
        manager_1 = EncryptionManager(key, iv)
        plaintext_1 = m1.read()
        ciphertext_1 = manager_1.update_encryptor(plaintext_1) + manager_1.finalize_encryptor()
        keystream = get_keastream(ciphertext_1, plaintext_1)

        with open('message_2.txt', 'rb') as m2:
            manager_2 = EncryptionManager(key, iv)
            plaintext_2 = m2.read()
            ciphertext_2a = manager_2.update_encryptor(plaintext_2) + manager_2.finalize_encryptor()
            deciphertext_2a = manager_2.update_decryptor(ciphertext_2a) + manager_2.finalize_decryptor()
            deciphertext_2b = xor_data(ciphertext_2a, keystream)

            if deciphertext_2a == deciphertext_2b:
                print('[PASS]')
            else:
                print('[FAIL]')

            print(deciphertext_2b.decode())

