import string

from cryptography.hazmat.primitives.ciphers import Cipher


def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter       = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]

        encoding[letter]       = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding

def encode_cmp(message, subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher


class EncryptorDecriptor:
    def __init__(self, key: bytes, cipher: Cipher):
        self.key = key
        self.cipher = cipher
        self.encryptor = self.cipher.encryptor()
        self.decryptor = self.cipher.decryptor()
