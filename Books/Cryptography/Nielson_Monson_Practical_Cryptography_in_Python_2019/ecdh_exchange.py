from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# from cryptography.hazmat.primitives.serialization import PublicFormat
# from cryptography.hazmat.primitives.serialization import Encoding

# Generate a private key for use in the exchange.
private_key = ec.generate_private_key(
    ec.SECP384R1(), default_backend()
)
# In a real handshake the peer_public_key will be received from the
# other party. For this example we'll generate another private key
# and get a public key from that.
peer_public_key = ec.generate_private_key(
    ec.SECP384R1(), default_backend()
).public_key()
shared_key = private_key.exchange(ec.ECDH(), peer_public_key)


# # save the public key in a file
# with open('public_key.pem', 'wb') as f:
#     f.write(peer_public_key.public_bytes(encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo))


# Perform key derivation.
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
    backend=default_backend()
).derive(shared_key)

# AUTO TEST
if len(derived_key) == 32:
    print("[PASS]")
else:
    print("[FAIL]")