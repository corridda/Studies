import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def xor_data(data:bytes, key:bytes):
    """XOR the data with the given key.

    :param data: data to be XORed (bytes)
    :param key: the key the data to be XORed with (bytes)
    """
    res = hex(int(data.hex(), base=16) ^ int(key.hex(), base=16))[2:]
    return '0' * (32 - len(res)) + res


class EncryptionManager:
    def __init__(self):
        key = os.urandom(16)
        self.iv  = os.urandom(16)
        aesContext = Cipher(algorithms.AES(key),
                            modes.ECB(),
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
    path = f"../aes_exercise_example/top_secrete.bmp"

    # cipher
    with open(path, 'rb') as inp:
        manager = EncryptionManager()
        image_data = inp.read()
        header, body = image_data[:54], image_data[54:]
        increment = b"\x00" * (16 - (len(body) % 16))
        body += increment

        CHUNK_SIZE = 16
        cur_idx = 0
        cur_vector = manager.iv
        ciphertext = header
        while True:
            cur_chunk = body[cur_idx : cur_idx+CHUNK_SIZE]
            cur_idx += CHUNK_SIZE
            if len(cur_chunk):
                inp_to_encryptor = bytes.fromhex(xor_data(cur_chunk, cur_vector))
            else:
                break
            cur_ciphered_chunk = manager.update_encryptor(inp_to_encryptor)
            cur_vector = cur_ciphered_chunk
            ciphertext += cur_ciphered_chunk

        ciphertext += manager.finalize_encryptor()

        with open('top_secrete_hand-crafted_CBC_encr.bmp', 'wb') as out:
            out.write(ciphertext)


        # decipher
        header, body = ciphertext[:54], ciphertext[54:]

        cur_idx = 0
        cur_vector = manager.iv
        deciphertext = header
        while True:
            cur_chunk = body[cur_idx : cur_idx+CHUNK_SIZE]
            cur_idx += CHUNK_SIZE
            if len(cur_chunk):
                cur_deciphered_chunk = manager.update_decryptor(cur_chunk)
                if len(cur_deciphered_chunk):
                    xor = bytes.fromhex(xor_data(cur_deciphered_chunk, cur_vector))
                    deciphertext += xor
                    cur_vector = prev_chunk
                prev_chunk = cur_chunk
            else:
                break

        deciphertext += manager.finalize_decryptor()

        with open('top_secrete_hand-crafted_CBC_decr.bmp', 'wb') as out:
            out.write(deciphertext[:-len(increment)])