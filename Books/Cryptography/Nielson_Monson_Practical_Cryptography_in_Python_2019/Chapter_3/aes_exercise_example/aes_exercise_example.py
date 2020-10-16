#! /usr/bin/env python3

import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_AES_CBC(ifile: str, ofile: str):
    test_key = os.urandom(16)
    aesCipher = Cipher(algorithms.AES(test_key),
                       modes.ECB(),
                       backend=default_backend())
    aesEncryptor = aesCipher.encryptor()

    with open(ifile, "rb") as reader:
        with open(ofile, "wb+") as writer:
            image_data = reader.read()
            header, body = image_data[:54], image_data[54:]
            body += b"\x00" * (16 - (len(body) % 16))
            writer.write(header + aesEncryptor.update(body))

if __name__ == '__main__':
    encrypt_AES_CBC('top_secrete.bmp', 'top_secrete_encrypted.bmp')