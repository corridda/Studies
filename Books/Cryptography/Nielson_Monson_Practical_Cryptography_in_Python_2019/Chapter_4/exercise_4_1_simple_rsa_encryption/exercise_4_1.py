#!/usr/bin/python3
__author__ = 'Igor Vasilev'


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


#### DANGER ####
# The following RSA encryption and decryption is
# completely unsafe and terribly broken. DO NOT USE
# for anything other than the practice exercise
################
def simple_rsa_encrypt(m, publickey):
    numbers = publickey.public_numbers()
    return pow(m, numbers.e, numbers.n)


def simple_rsa_decrypt(c, privatekey):
    numbers = privatekey.private_numbers()
    return pow(c, numbers.d, numbers.public_numbers.n)
#### DANGER ####


def int_to_bytes(i):
    i = int(i)
    return i.to_bytes((i.bit_length() + 7) // 8, byteorder='big')


def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')


def main():
    message = b"Test message"

    # Create new public and private keys.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt Message
    message_as_int = bytes_to_int(message)
    cipher_as_int = simple_rsa_encrypt(message_as_int, public_key)
    cipher = int_to_bytes(cipher_as_int)

    # Decrypt Message
    cipher_as_int = bytes_to_int(cipher)
    message_as_int = simple_rsa_decrypt(cipher_as_int, private_key)
    decyphered_message = int_to_bytes(message_as_int)


    if message != decyphered_message:
        print("[FAIL]")
    else:
        print("[PASS]")


if __name__ == '__main__':
    main()
