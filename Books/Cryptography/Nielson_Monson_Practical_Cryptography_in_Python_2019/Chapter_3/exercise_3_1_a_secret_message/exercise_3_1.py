from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


class EncryptorDecriptor:
    def __init__(self, key: bytes, cipher: Cipher):
        self.key = key
        self.cipher = cipher
        self.encryptor = self.cipher.encryptor()
        self.decryptor = self.cipher.decryptor()


key = os.urandom(16)
aesCipher = Cipher(algorithms.AES(key),
                   modes.ECB(),
                   backend=default_backend())
encr_decr = EncryptorDecriptor(key=key, cipher=aesCipher)
