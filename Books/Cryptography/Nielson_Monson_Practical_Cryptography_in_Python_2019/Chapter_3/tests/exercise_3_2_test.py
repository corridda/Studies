from random import choices
from string import ascii_uppercase

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from Books.Cryptography.Nielson_Monson_Practical_Cryptography_in_Python_2019.Chapter_3. \
    exercise_3_2_updated_technology.exercise_3_2 \
    import EncryptorDecriptor, create_shift_substitutions, encode_cmp

subst, unsubst = create_shift_substitutions(10)


class TestClass:
    def test_1(self):
        message = b'a secret message'
        key = bytes(encode_cmp(message.decode(encoding='utf-8').upper(), subst), encoding='utf-8')
        aesCipher = Cipher(algorithms.AES(key),
                           modes.ECB(),
                           backend=default_backend())
        encr_decr = EncryptorDecriptor(key=key, cipher=aesCipher)
        assert encr_decr.decryptor.update(encr_decr.encryptor.update(message)) == message

    def test_2(self):
        message = bytes(''.join(choices(ascii_uppercase, k=16)), encoding='utf-8')
        key = bytes(encode_cmp(message.decode(encoding='utf-8'), subst), encoding='utf-8')
        aesCipher = Cipher(algorithms.AES(key),
                           modes.ECB(),
                           backend=default_backend())
        encr_decr = EncryptorDecriptor(key=key, cipher=aesCipher)
        assert encr_decr.decryptor.update(encr_decr.encryptor.update(message)) == message
