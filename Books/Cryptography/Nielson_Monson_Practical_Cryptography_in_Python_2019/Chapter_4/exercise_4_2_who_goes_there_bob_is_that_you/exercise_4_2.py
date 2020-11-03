#!/usr/bin/python3
__author__ = 'Igor Vasilev'

from hashlib import sha256

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat


class Person:
    def __init__(self):
        self.public_key, self.private_key = self._get_keys()

    def _get_keys(self):
        # Create new public and private keys.
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return public_key, private_key

    def get_other_person_PK(self, other_person):
        return other_person.public_key


if __name__ == '__main__':
    alice = Person()
    bob = Person()
    eve = Person()

    eve_public_key = eve.public_key.public_bytes(encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo)

    # Eve is changing alice's and bob's public keys with her own public key to be able
    # to employ a very tricky subterfuge
    kinda_alices_pk, kinda_bobs_pk = bob.get_other_person_PK(eve), alice.get_other_person_PK(eve)
    kinda_alices_pk_bytes = \
        kinda_alices_pk.public_bytes(encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo)

    kinda_bobs_pk_bytes = \
        kinda_bobs_pk.public_bytes(encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo)

    if sha256(eve_public_key).hexdigest() == sha256(kinda_alices_pk_bytes).hexdigest() \
        == sha256(kinda_bobs_pk_bytes).hexdigest():
        print(f"[PASS]")
    else:
        print(f"[FAIL]")