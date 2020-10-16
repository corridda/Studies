"""EXERCISE 3.17. VISUALIZING CIPHERTEXT CHANGES
To better understand the difference between counter mode and cipher block chaining mode,
go back to the image encryption utility you wrote previously. Modify it to first encrypt and
then decrypt the image, using either AES-CBC or AES-CTR as the mode. After decryption, the
original image should be completely restored.
Now introduce an error into the ciphertext and decrypt the modified bytes. Try, for example,
picking the byte right in the middle of the encrypted image data and setting it to 0. After
corrupting the data, call the decryption function and view the restored image. How much of a
difference did the edit make with CTR? How much of a difference did the edit make with CBC?
Hint: if you can’t see anything, try an all-white image. if you still can’t see it, change 50
bytes or so to figure out where the changes are happening. Once you find where the changes
are happening, go back to changing a single byte to view the differences between CTR and
CBC. Can you explain what’s happening?"""