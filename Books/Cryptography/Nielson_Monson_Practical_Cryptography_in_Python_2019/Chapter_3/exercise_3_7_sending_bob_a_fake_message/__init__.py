"""EXERCISE 3.7. SENDING BOB A FAKE MESSAGE

Take two different ciphertexts from alice to Bob with different meeting instructions on different
dates. Splice the ciphertext from the body of the first message into the body of the second
message. That is, start by replacing the last block of the newer message with the last block (or
blocks if it was longer) of the previous message. Does the message decrypt? Did you change
where Bob goes to meet Alice?"""