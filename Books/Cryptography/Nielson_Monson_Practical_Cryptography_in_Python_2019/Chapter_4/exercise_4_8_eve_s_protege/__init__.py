"""EXERCISE 4.8. EVE’S PROTEGE
Recreate Eve’s chosen ciphertext attack. Create a sample message in python, as you have
done previously, using the public key to encrypt it. Then, encrypt a value of r (such as 2).
Multiply the two numeric versions of the ciphertext together and don’t forget to take the
answer modulo n. Decrypt this new ciphertext and try to convert it to bytes. It shouldn’t be
anything human readable. Take the numeric version of this decryption and multiply it by the
inverse of r (mod n). You should be back to the original number. Convert it to bytes to see the
original message"""