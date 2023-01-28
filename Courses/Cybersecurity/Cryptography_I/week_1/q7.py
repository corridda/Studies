"""Suppose you are told that the one time pad encryption of the message "attack at dawn"
is 09e1c5f70a65ac519458e7e53f36 (the plaintext letters are encoded as 8-bit ASCII and the given
ciphertext is written in hex). What would be the one time pad encryption of the message "attack at dusk"
under the same OTP key?"""

m1 = "attack at dawn"
m2 = "attack at dusk"
c1 = '09e1c5f70a65ac519458e7e53f36'

m1_hex = bytes([ord(ch) for ch in m1]).hex()
m2_hex = bytes([ord(ch) for ch in m2]).hex()
k = int(m1_hex, base=16) ^ int(c1, base=16)
c2 = (int(m2_hex, base=16) ^ k).to_bytes(14, byteorder='big').hex()
print(c2)