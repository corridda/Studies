import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes



def f2(x: bytes, y: bytes) -> bytes:
    cipher =Cipher(algorithm=algorithms.AES(x), mode=modes.ECB())
    encryptor = cipher.encryptor()
    ct = encryptor.update(x) + encryptor.finalize()
    return (int.from_bytes(ct, byteorder='big') ^ int.from_bytes(y, byteorder='big'))\
        .to_bytes(16, byteorder='big')

def check_f2(x1: bytes, x2: bytes, y1: bytes, y2: bytes,) -> bool:
    first = f2(x1, y1)
    second = f2(x2, y2)
    # print(f"first:\t{first.hex()}\nsecond:\t{second.hex()}")
    return first == second


if __name__ == '__main__':
    # Case 1
    # *   Choose x1,x2,y1 arbitrarily (with x1 != x2)
    #     Set y2 = AES(x1, x1) ⊕ AES(x2, x2)
    x1 = os.urandom(16)
    x2 = os.urandom(16)
    y1 = os.urandom(16)
    while x1 == x2:
        x2 = os.urandom(16)

    cipher1 =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher1.encryptor()
    y2_1 = encryptor.update(x1) + encryptor.finalize()

    cipher2 =Cipher(algorithm=algorithms.AES(x2), mode=modes.ECB())
    encryptor = cipher2.encryptor()
    y2_2 = encryptor.update(x2) + encryptor.finalize()

    y2 = (int.from_bytes(y2_1, byteorder='big') ^ int.from_bytes(y2_2, byteorder='big'))\
        .to_bytes(16, byteorder='big')
    print(f"Case 1\n"
          f"f(y1,x1) == f1(y2, x2): {check_f2(x1, x2, y1, y2)}\n")


    # Case 2
    # *   Choose x1,y1,x2 arbitrarily (with x1 != x2)
    #     Set y2 = y1 ⊕ AES(x1, x1)
    x1 = os.urandom(16)
    x2 = os.urandom(16)
    y1 = os.urandom(16)
    while x1 == x2:
        x2 = os.urandom(16)

    cipher =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher.encryptor()
    y2_2 = encryptor.update(x1) + encryptor.finalize()

    y2 = (int.from_bytes(y1, byteorder='big') ^ int.from_bytes(y2_2, byteorder='big'))\
        .to_bytes(16, byteorder='big')
    print(f"Case 1\n"
          f"f(y1,x1) == f1(y2, x2): {check_f2(x1, x2, y1, y2)}\n")


    # Case 3
    # *   Choose x1,y1,x2 arbitrarily (with x1 != x2)
    #     Set y2 = y1 ⊕ AES(x1, x1) ⊕ AES(x2, x2)
    x1 = os.urandom(16)
    x2 = os.urandom(16)
    y1 = os.urandom(16)
    while x1 == x2:
        x2 = os.urandom(16)

    cipher =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher.encryptor()
    v = encryptor.update(y1) + encryptor.finalize()

    cipher1 =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher1.encryptor()
    y2_2 = encryptor.update(x1) + encryptor.finalize()

    cipher2 =Cipher(algorithm=algorithms.AES(x2), mode=modes.ECB())
    encryptor = cipher2.encryptor()
    y2_3 = encryptor.update(x2) + encryptor.finalize()

    y2 = (int.from_bytes(y1, byteorder='big') ^ int.from_bytes(y2_2, byteorder='big')
          ^ int.from_bytes(y2_3, byteorder='big'))\
        .to_bytes(16, byteorder='big')
    print(f"Case 3\n"
          f"f(y1,x1) == f1(y2, x2): {check_f2(x1, x2, y1, y2)}\n")

    # Case 4
    # *   Choose x1,y1,x2 arbitrarily (with x1 != x2)
    #     Set y2 = y1 ⊕ x1 ⊕ AES(x2, x2)
    x1 = os.urandom(16)
    x2 = os.urandom(16)
    y1 = os.urandom(16)
    while x1 == x2:
        x2 = os.urandom(16)

    cipher =Cipher(algorithm=algorithms.AES(x2), mode=modes.ECB())
    encryptor = cipher.encryptor()
    y2_3 = encryptor.update(x2) + encryptor.finalize()

    y2 = (int.from_bytes(y1, byteorder='big') ^ int.from_bytes(x1, byteorder='big')
          ^ int.from_bytes(y2_3, byteorder='big'))\
        .to_bytes(16, byteorder='big')
    print(f"Case 4\n"
          f"f(y1,x1) == f1(y2, x2): {check_f2(x1, x2, y1, y2)}\n")
