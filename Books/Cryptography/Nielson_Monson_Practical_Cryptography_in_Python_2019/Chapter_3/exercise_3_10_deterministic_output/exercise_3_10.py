from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
from pprint import pprint

class EncryptionManager:
    def __init__(self):
        self.key = os.urandom(32)
        self.iv  = os.urandom(16)

    def encrypt_message(self, message):
        # WARNING: This code is not secure!!
        encryptor = Cipher(algorithms.AES(self.key),
                           modes.CBC(self.iv),
                           backend=default_backend()).encryptor()
        padder = padding.PKCS7(128).padder()

        padded_message = padder.update(message)
        padded_message += padder.finalize()
        ciphertext = encryptor.update(padded_message)
        ciphertext += encryptor.finalize()
        return ciphertext

    def decrypt_message(self, ciphertext):
        # WARNING: This code is not secure!!
        decryptor = Cipher(algorithms.AES(self.key),
                           modes.CBC(self.iv),
                           backend=default_backend()).decryptor()
        unpadder = padding.PKCS7(128).unpadder()

        padded_message = decryptor.update(ciphertext)
        padded_message += decryptor.finalize()
        message = unpadder.update(padded_message)
        message += unpadder.finalize()
        return message


# Automatically generate key/IV for encryption
test_manager = EncryptionManager()
ciphertexts = []
message = os.urandom(16)
ciphertexts.append(test_manager.encrypt_message(message))
ciphertexts.append(test_manager.encrypt_message(message))
ciphertexts.append(test_manager.encrypt_message(message))
ciphertexts.append(test_manager.encrypt_message(message))

hex_ciphertexts = [c.hex() for c in ciphertexts]
pprint(hex_ciphertexts)

if hex_ciphertexts[0] == hex_ciphertexts[1] == hex_ciphertexts[2] == hex_ciphertexts[3]:
    print(f"\n[PASS]")
else:
    print(f"\n[FAIL]")