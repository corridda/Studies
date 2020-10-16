"""EXERCISE 3.15. RIDING THE KEYSTREAM
Put into practice this keystream-stealing attack. That is, encrypt two different purchase
messages using the same key and IV. “Intercept” one of the two messages and XOR the
ciphertext contents with the known plaintext. This will give you a keystream. Next, XOR the
keystream with the other message to recover that message’s plaintext. The message sizes
may be a little different, but if you’re short some keystream bytes, recover what you can.
"""