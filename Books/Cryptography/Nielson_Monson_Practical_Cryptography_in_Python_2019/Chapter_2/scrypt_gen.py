import os
import traceback as tb

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey

salt = os.urandom(16)

kdf = Scrypt(salt=salt, length=32,
                n=2**14, r=8, p=1,
                backend=default_backend())

key = kdf.derive(b"my great password")
print("KDF output:", key.hex())

kdf = Scrypt(salt=salt, length=32,
             n=2**14, r=8, p=1,
             backend=default_backend())

try:
    kdf.verify(b"my great password", key)
    print("Success! (Exception if mismatch)")
    # If we got here, we passed
    print("[PASS]")
except InvalidKey:
    tb.print_exc()


