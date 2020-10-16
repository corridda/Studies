"""EXERCISE 3.12. HAND-CRAFTED CBC
ECB mode is just raw AES. You can create your own CBC mode using ECB as the building
block. For this exercise, see if you can build a CBC encryption and decryption operation that
is compatible with the 'cryptography' library. For encryption, remember to take the output
of each block and XOR it with the plaintext of the next block before encryption. Reverse the
process for decryption.
"""