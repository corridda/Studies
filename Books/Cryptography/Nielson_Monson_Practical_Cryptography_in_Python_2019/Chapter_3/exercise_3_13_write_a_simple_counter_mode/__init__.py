"""EXERCISE 3.13. WRITE A SIMPLE COUNTER MODE

As you did with CBC, create counter mode encryption from ECB mode. This should be even
easier than it was with CBC. Generate the key stream by taking the IV block and encrypting
it, then increasing the value of the IV block by one to generate the next block of key stream
material. When finished, XOR the key stream with the plaintext. Decrypt in the same manner.
"""