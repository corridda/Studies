from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def main():
    message = b'Test message'

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None  # rarely used. Just leave it 'None'
        )
    )

    recovered = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None  # rarely used. Just leave it 'None'
        ))

    print(f"Plaintext: {message}")
    print(f"Ciphertext with OAEP padding (hexlified):\n{ciphertext.hex()}")
    print(f"Recovered: {recovered}\n")

    if recovered == message:
        print("[PASS]")
    else:
        print("[FAIL]")


if __name__ == "__main__":
    main()
