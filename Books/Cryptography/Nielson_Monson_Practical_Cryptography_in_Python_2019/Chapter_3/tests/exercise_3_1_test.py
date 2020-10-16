from random import choices
from string import printable


from Books.Cryptography.Nielson_Monson_Practical_Cryptography_in_Python_2019.Chapter_3. \
    exercise_3_1_a_secret_message.exercise_3_1 import encr_decr


class TestClass:
    def test_1(self):
        message = b'a secret message'
        assert encr_decr.decryptor.update(encr_decr.encryptor.update(message)) == message

    def test_2(self):
        message = bytes(''.join(choices(printable, k=16)), encoding='utf-8')
        assert encr_decr.decryptor.update(encr_decr.encryptor.update(message)) == message
