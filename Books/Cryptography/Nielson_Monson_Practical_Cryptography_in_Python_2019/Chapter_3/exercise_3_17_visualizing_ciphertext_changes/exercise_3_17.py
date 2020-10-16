import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def xor_data(data:bytes, key:bytes):
    """XOR the data with the given key.

    :param data: data to be XORed (bytes)
    :param key: the key the data to be XORed with (bytes)
    """
    return bytes(pair[0] ^ pair[1] for pair in zip(data, key))


class ModeError(Exception):
    def __init__(self):
        super().__init__('Inappropriate mode!')


class EncryptionManager:
    def __init__(self, mode: str):
        self.key = os.urandom(16)
        self.iv  = os.urandom(16)
        if mode.strip().upper() == 'CTR':
            self.mode = modes.CTR
            print(f"self.mode: {self.mode}")
        elif mode.strip().upper() == 'CBC':
            self.mode = modes.CBC
            print(f"self.mode: {self.mode}")
        else:
            raise ModeError
        aesContext = Cipher(algorithms.AES(self.key),
                            self.mode(self.iv),
                            backend=default_backend())
        self.encryptor = aesContext.encryptor()
        self.decryptor = aesContext.decryptor()
        self.padder = padding.PKCS7(128).padder()
        self.unpadder = padding.PKCS7(128).unpadder()

    def update_encryptor(self, plaintext):
        if self.mode == modes.CBC:
            return self.encryptor.update(self.padder.update(plaintext))
        else:
            return self.encryptor.update(plaintext)

    def finalize_encryptor(self):
        if self.mode == modes.CBC:
            return self.encryptor.update(self.padder.finalize()) + self.encryptor.finalize()
        else:
            return self.encryptor.finalize()

    def update_decryptor(self, ciphertext):
        if self.mode == modes.CBC:
            return self.unpadder.update(self.decryptor.update(ciphertext))
        else:
            return self.decryptor.update(ciphertext)

    def finalize_decryptor(self):
        if self.mode == modes.CBC:
            return self.unpadder.update(self.decryptor.finalize()) + self.unpadder.finalize()
        else:
            return self.decryptor.finalize()


if __name__ == '__main__':
    path = f"../aes_exercise_example/top_secrete.bmp"

    times = []
    with open(path, 'rb') as inp:
        image_data = inp.read()
        header, body = image_data[:54], image_data[54:]


        """Proper CTR encryption - decryption"""
        # cipher
        manager = EncryptionManager(mode='CTR')
        ciphertext = header + manager.update_encryptor(body) + manager.finalize_encryptor()

        with open('top_secrete_CTR_encr.bmp', 'wb') as out:
            out.write(ciphertext)

        # decipher
        header, body = ciphertext[:54], ciphertext[54:]
        deciphertext = header + manager.update_decryptor(body) + manager.finalize_decryptor()

        with open('top_secrete_CTR_decr.bmp', 'wb') as out:
            out.write(deciphertext)


        """CTR decryption of a corrupted CTR-encrypted file"""
        header, body = image_data[:54], image_data[54:]

        # cipher
        manager = EncryptionManager(mode='CTR')
        ciphertext = manager.update_encryptor(body) + manager.finalize_encryptor()
        corrupted_body = ciphertext[:(len(ciphertext) // 2) - 500] + b'0' * 1000 + \
                         ciphertext[(len(ciphertext) // 2) + 500:]
        ciphertext_corrupted = header + corrupted_body

        with open('top_secrete_CTR_encr_corrupted.bmp', 'wb') as out:
            out.write(ciphertext_corrupted)

        # decipher
        header, corrupted_body = ciphertext_corrupted[:54], ciphertext_corrupted[54:]
        deciphertext = header + manager.update_decryptor(corrupted_body) + manager.finalize_decryptor()

        with open('top_secrete_CTR_decr_corrupted.bmp', 'wb') as out:
            out.write(deciphertext)


        # """Proper CBC encryption - decryption"""
        # header, body = image_data[:54], image_data[54:]
        #
        # # cipher
        # manager = EncryptionManager(mode='CBC')
        # ciphertext = header + manager.update_encryptor(body) + manager.finalize_encryptor()
        #
        # with open('top_secrete_CBC_encr.bmp', 'wb') as out:
        #     out.write(ciphertext)
        #
        # # decipher
        # header, body = ciphertext[:54], ciphertext[54:]
        # deciphertext = header + manager.update_decryptor(body) + manager.finalize_decryptor()
        #
        # with open('top_secrete_CBC_decr.bmp', 'wb') as out:
        #     out.write(deciphertext)


        """CBC decryption of a corrupted CBC-encrypted file"""
        header, body = image_data[:54], image_data[54:]

        # cipher
        manager = EncryptionManager(mode='CBC')
        ciphertext = manager.update_encryptor(body) + manager.finalize_encryptor()
        corrupted_body = ciphertext[:(len(ciphertext) // 2) - 500] + b'0' * 1000 + \
                         ciphertext[(len(ciphertext) // 2) + 500:]
        ciphertext_corrupted = header + corrupted_body

        with open('top_secrete_CBC_encr_corrupted.bmp', 'wb') as out:
            out.write(ciphertext_corrupted)

        # decipher
        header, corrupted_body = ciphertext_corrupted[:54], ciphertext_corrupted[54:]
        deciphertext = header + manager.update_decryptor(corrupted_body) + manager.finalize_decryptor()

        with open('top_secrete_CBC_decr_corrupted.bmp', 'wb') as out:
            out.write(deciphertext)
