import os
from time import perf_counter
from statistics import mean
from multiprocessing import Pool

import psutil

# ray requires >= Python 3.6 and <= Python 3.8 (status: 2020-10-11)
# import ray

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
    def __init__(self, key, iv):
        self.key = key
        self.iv  = iv
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


def keystream(key, iv, body, CHUNK_SIZE, counter_first, counter_last):
    manager = EncryptionManager(key, iv)
    cur_idx = counter_first * CHUNK_SIZE
    counter = counter_first
    cur_vector = iv
    ciphertext = b''
    while counter <= counter_last:
        fx = hex(int(cur_vector.hex(), base=16) + counter)[2:]
        fx = '0' * (32 - len(fx)) + fx
        cur_vector = bytes.fromhex(fx)
        counter += 1
        encrypted_cur_vector = manager.update_encryptor(cur_vector)
        cur_chunk = body[cur_idx: cur_idx + CHUNK_SIZE]
        cur_idx += CHUNK_SIZE
        if len(cur_chunk):
            encrypted_chunk = bytes.fromhex(xor_data(cur_chunk, encrypted_cur_vector))
            ciphertext += encrypted_chunk
        else:
            break
    return ciphertext

# @ray.remote
# def keystream_ray(key, iv, body, CHUNK_SIZE, counter_first, counter_last):
#     manager = EncryptionManager(key, iv)
#     cur_idx = counter_first * CHUNK_SIZE
#     counter = counter_first
#     cur_vector = iv
#     ciphertext = b''
#     while counter <= counter_last:
#         fx = hex(int(cur_vector.hex(), base=16) + counter)[2:]
#         fx = '0' * (32 - len(fx)) + fx
#         cur_vector = bytes.fromhex(fx)
#         counter += 1
#         encrypted_cur_vector = manager.update_encryptor(cur_vector)
#         cur_chunk = body[cur_idx: cur_idx + CHUNK_SIZE]
#         cur_idx += CHUNK_SIZE
#         if len(cur_chunk):
#             encrypted_chunk = bytes.fromhex(xor_data(cur_chunk, encrypted_cur_vector))
#             ciphertext += encrypted_chunk
#         else:
#             break
#     return ciphertext

if __name__ == '__main__':
    path = f"../aes_exercise_example/top_secrete.bmp"
    test_number = 10

    """multiprocessing.Pool"""
    make_files = False

    times = []
    with open(path, 'rb') as inp:
        image_data = inp.read()
        header, body = image_data[:54], image_data[54:]
        increment = b"\x00" * (16 - (len(body) % 16))
        body += increment

        CHUNK_NUMBER = len(body) // 16

        # The number of usable CPUs
        CPU_NUM = len(psutil.Process().cpu_affinity())
        print(f"CPU_NUM: {CPU_NUM}")

        key = os.urandom(16)
        iv = os.urandom(16)

        for _ in range(test_number):
            start = perf_counter()

            # cipher
            CHUNK_SIZE = 16
            t = CHUNK_NUMBER // CPU_NUM
            set_of_counters = [
                (t * i, t * i + t - 1) if i < (CPU_NUM - 1) else (t * i, CHUNK_NUMBER) \
                for i in range(CPU_NUM)
            ]
            ciphertext = header

            args = []
            for s in set_of_counters:
                args.append((key, iv, body, CHUNK_SIZE, s[0], s[1]))

            with Pool(CPU_NUM) as p:
                results = p.starmap_async(keystream, args).get()
                for res in results:
                    ciphertext += res

            if make_files:
                with open('top_secrete_hand-crafted_CTR_encr.bmp', 'wb') as out:
                    out.write(ciphertext)

            # decipher
            header, body = ciphertext[:54], ciphertext[54:]
            args = []
            for s in set_of_counters:
                args.append((key, iv, body, CHUNK_SIZE, s[0], s[1]))
            deciphertext = header
            with Pool(CPU_NUM) as p:
                results = p.starmap_async(keystream, args).get()
                for res in results:
                    deciphertext += res

            if make_files:
                with open('top_secrete_hand-crafted_CTR_decr.bmp', 'wb') as out:
                    out.write(deciphertext[:-len(increment)])
                make_files = False

            times.append(perf_counter() - start)
        print(f"multiprocessing.Pool average time: {mean(times)}\n")


    # """ray"""
    # ray.init()
    # make_files = False
    # times = []
    # with open(path, 'rb') as inp:
    #     image_data = inp.read()
    #     header, body = image_data[:54], image_data[54:]
    #     increment = b"\x00" * (16 - (len(body) % 16))
    #     body += increment
    #
    #     CHUNK_NUMBER = len(body) // 16
    #
    #     # The number of usable CPUs
    #     CPU_NUM = len(psutil.Process().cpu_affinity())
    #     print(f"CPU_NUM: {CPU_NUM}")
    #
    #     key = os.urandom(16)
    #     iv = os.urandom(16)
    #
    #     for _ in range(test_number):
    #         start = perf_counter()
    #
    #         # cipher
    #         CHUNK_SIZE = 16
    #         t = CHUNK_NUMBER // CPU_NUM
    #         set_of_counters = [
    #             (t * i, t * i + t - 1) if i < (CPU_NUM - 1) else (t * i, CHUNK_NUMBER) \
    #             for i in range(CPU_NUM)
    #         ]
    #         ciphertext = header
    #
    #         args = []
    #         for s in set_of_counters:
    #             args.append((key, iv, body, CHUNK_SIZE, s[0], s[1]))
    #
    #         streams = [keystream_ray.remote(*s) for s in args]
    #         results = ray.get(streams)
    #         for res in results:
    #             ciphertext += res
    #
    #         if make_files:
    #             with open('top_secrete_hand-crafted_CTR_encr.bmp', 'wb') as out:
    #                 out.write(ciphertext)
    #
    #         # decipher
    #         header, body = ciphertext[:54], ciphertext[54:]
    #         args = []
    #         for s in set_of_counters:
    #             args.append((key, iv, body, CHUNK_SIZE, s[0], s[1]))
    #         deciphertext = header
    #         streams = [keystream_ray.remote(*s) for s in args]
    #         results = ray.get(streams)
    #         for res in results:
    #             deciphertext += res
    #
    #         if make_files:
    #             with open('top_secrete_hand-crafted_CTR_decr.bmp', 'wb') as out:
    #                 out.write(deciphertext[:-len(increment)])
    #             make_files = False
    #
    #         times.append(perf_counter() - start)
    #     print(f"ray average time: {mean(times)}")