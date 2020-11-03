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
    message_1 = b'Test message'
    r = b'2'

    # Create new public and private keys.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    n = public_key.public_numbers().n
    print(f"n: {n}")

    # Encrypt message_1
    message_1_as_int = bytes_to_int(message_1)
    cipher_as_int_1 = simple_rsa_encrypt(message_1_as_int, public_key)

    # Encrypt r
    r_as_int = bytes_to_int(r)
    cipher_as_int_2 = simple_rsa_encrypt(r_as_int, public_key)

    # cipher_1 * cipher_2 (mod n)
    cipher_1_cipher_2_mult = (cipher_as_int_1 * cipher_as_int_2) % n

    # Decrypt cipher_1 * cipher_2
    decr_cipher_1_cipher_2_mult_as_int = simple_rsa_decrypt(cipher_1_cipher_2_mult, private_key)

    # Inverse of r (mod n)
    r_inv_modulo_n = pow(bytes_to_int(r), -1, n)

    if int_to_bytes((decr_cipher_1_cipher_2_mult_as_int * r_inv_modulo_n) % n) != message_1:
        print("[FAIL]")
    else:
        print("[PASS]")


if __name__ == '__main__':
    main()
