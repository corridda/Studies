import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


class EncryptionManager:
    def __init__(self):
        key = os.urandom(32)
        iv  = os.urandom(16)
        aesContext = Cipher(algorithms.AES(key),
                            modes.CBC(iv),
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


if __name__ == '__main__':
    # Auto generate key/IV for encryption
    manager = EncryptionManager()

    path = f"../aes_exercise_example/top_secrete.bmp"
    with open(path, 'rb') as inp:
        image_data = inp.read()
        header, body = image_data[:54], image_data[54:]
        increment = b"\x00" * (16 - (len(body) % 16))
        body += increment
        ciphertext = header + manager.update_encryptor(body)
        ciphertext += manager.finalize_encryptor()
        with open('top_secrete_CBC_encr.bmp', 'wb') as out1:
            out1.write(ciphertext)
        with open('top_secrete_decr.bmp', 'wb') as out2:
            header, body = ciphertext[:54], ciphertext[54:]
            deciphered = header + manager.update_decryptor(body)
            deciphered += manager.finalize_decryptor()
            out2.write(deciphered[:-len(increment)])


    with open(path, 'rb') as f1:
        with open('top_secrete_CBC_decr.bmp', 'rb') as f2:
            cont_1 = f1.read()
            cont_2 = f2.read()

            if cont_1 == cont_2:
                print("[PASS]")
            else:
                for c1, c2 in zip(cont_1, cont_2):
                    if c1 != c2:
                        print("Mismatch", c1, c2)
                print("[FAIL]")