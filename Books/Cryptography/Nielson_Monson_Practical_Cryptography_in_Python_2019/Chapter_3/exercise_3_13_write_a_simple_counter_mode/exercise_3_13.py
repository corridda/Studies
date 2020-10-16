import os
from time import perf_counter
from statistics import mean

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


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

    def update_encryptor(self, plaintext):
        return self.encryptor.update(plaintext)

    def finalize_encryptor(self):
        return self.encryptor.update(self.encryptor.finalize())

    def update_decryptor(self, ciphertext):
        return self.decryptor.update(ciphertext)

    def finalize_decryptor(self):
        return self.decryptor.finalize()


if __name__ == '__main__':
    path = f"../aes_exercise_example/top_secrete.bmp"
    # make_files = True
    make_files = False

    times = []
    with open(path, 'rb') as inp:
        image_data = inp.read()
        header, body = image_data[:54], image_data[54:]
        increment = b"\x00" * (16 - (len(body) % 16))
        body += increment

        for _ in range(15):
            start = perf_counter()
            # cipher
            manager = EncryptionManager()
            CHUNK_SIZE = 16
            cur_idx = 0
            counter = 0
            cur_vector = manager.iv
            ciphertext = header
            while True:
                fx = hex(int(cur_vector.hex(), base=16) + counter)[2:]
                fx = '0' * (32 - len(fx)) + fx
                cur_vector = bytes.fromhex(fx)
                counter += 1
                encrypted_cur_vector = manager.update_encryptor(cur_vector)
                cur_chunk = body[cur_idx : cur_idx+CHUNK_SIZE]
                cur_idx += CHUNK_SIZE
                if len(cur_chunk):
                    encrypted_chunk = bytes.fromhex(xor_data(cur_chunk, encrypted_cur_vector))
                    ciphertext += encrypted_chunk
                else:
                    break

            if make_files:
                with open('top_secrete_hand-crafted_CTR_encr.bmp', 'wb') as out:
                    out.write(ciphertext)

            # decipher
            header, body = ciphertext[:54], ciphertext[54:]

            cur_idx = 0
            counter = 0
            cur_vector = manager.iv
            deciphertext = header
            while True:
                fx = hex(int(cur_vector.hex(), base=16) + counter)[2:]
                fx = '0' * (32 - len(fx)) + fx
                cur_vector = bytes.fromhex(fx)
                counter += 1
                encrypted_cur_vector = manager.update_encryptor(cur_vector)
                cur_chunk = body[cur_idx : cur_idx+CHUNK_SIZE]
                cur_idx += CHUNK_SIZE
                if len(cur_chunk):
                    decrypted_chunk = bytes.fromhex(xor_data(cur_chunk, encrypted_cur_vector))
                    deciphertext += decrypted_chunk
                else:
                    break

            if make_files:
                with open('top_secrete_hand-crafted_CTR_decr.bmp', 'wb') as out:
                    out.write(deciphertext[:-len(increment)])
                make_files = False

            times.append(perf_counter() - start)
        print(f"average time: {mean(times)}")
