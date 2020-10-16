#! /usr/bin/env python3

"""XORing a plaintext."""
__author__ = 'Igor Vasilev'

import os
from random import choices
import string

def xor_data(data:bytes, key:bytes):
    """XOR the data with the given key.

    :param data: data to be XORed (bytes)
    :param key: the key the data to be XORed with (bytes)
    """
    return hex(int(data.hex(), base=16) ^ int(key.hex(), base=16))[2:]


if __name__ == '__main__':
    data = bytes(''.join(choices(string.ascii_letters, k=16)), encoding='utf-8')
    key = os.urandom(16)

    # XOR data with the key and then XOR the output the key
    if xor_data(bytes.fromhex(xor_data(data, key)), key) == data.hex():
        print('[PASS]')
    else:
        print('[FAIL]')
