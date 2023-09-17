"""EXERCISE 3.21. PREDICTING TIME-BASED RANDOMNESS
Write an AES encryption program (or modify one of the others you’ve written for this chapter)
that uses the python random number generator to generate keys. Use the seed method to
explicitly configure the generator based on the current time using time.time() rounded to
the nearest second. Then use this generator to create a key and encrypt some data. Write a
separate program that takes the encrypted data as input and tries to guess the key. It should
take a minimum time and a maximum time as a range and try iterating between these two
points as seed values for random"""