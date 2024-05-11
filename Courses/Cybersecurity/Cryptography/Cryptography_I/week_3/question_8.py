"""
8. In this question  you are asked to find a collision for the compression function:
f1(x, y) = AES(y,x) ⨁ y,
where AES(x,y) is the AES-128 encryption of y under key x.

Your goal is to find two distinct pairs (x1, y1) and (x2, y2)
such that f1(x1, y1) = f1(x2, y2)

Which of the following methods finds the required (x1, y1) and (x2, y2)?

*   Choose x1,y1,y2 arbitrarily (with y1 != y2) and let v := AES(y1,x1)
    Set x2 = AES^{−1}(y2, v ⊕ y1)

*   Choose x1,y1,x2 arbitrarily (with x1 != x2) and let v := AES(y1,x1)
    Set y2 = AES^{-1}(x2,v ⊕ y1 ⊕ x2)

*   Choose x1,y1,y2 arbitrarily (with y1 != y2) and let v := AES(y1,x1).
    Set x2 = AES^{-1}(y2,v ⊕ y1 ⊕ y2)

*   Choose x1,y1,y2 arbitrarily (with y1 != y2) and let v := AES(y1,x1).
    Set x2 = AES^{-1}(y2, v ⊕ y2)

"""

import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes



def f1(x: bytes, y: bytes) -> bytes:
    cipher =Cipher(algorithm=algorithms.AES(x), mode=modes.ECB())
    encryptor = cipher.encryptor()
    ct = encryptor.update(y) + encryptor.finalize()
    return (int.from_bytes(ct, byteorder='big') ^ int.from_bytes(y, byteorder='big'))\
        .to_bytes(16, byteorder='big')

def check_f1(y1: bytes, y2: bytes, x1: bytes, x2: bytes) -> bool:
    first = f1(x1, y1)
    second = f1(x2, y2)
    # print(f"first:\t{first.hex()}\nsecond:\t{second.hex()}")
    return first == second


if __name__ == '__main__':
    # Case 1
    # *   Choose x1,y1,y2 arbitrarily (with y1 != y2) and let v := AES(y1,x1)
    #     Set x2 = AES^{−1}(y2, v ⊕ y1)
    x1 = os.urandom(16)     # key
    y1 = os.urandom(16)
    y2 = os.urandom(16)
    while y1 == y2:
        y2 = os.urandom(16)

    cipher =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher.encryptor()
    v = encryptor.update(y1) + encryptor.finalize()

    key = (int.from_bytes(v, byteorder='big') ^ int.from_bytes(y1, byteorder='big'))\
        .to_bytes(16, byteorder='big')
    cipher2 = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
    decryptor = cipher2.decryptor()
    x2 = decryptor.update(y2) + decryptor.finalize()
    print(f"Case 1\n"
          f"f(y1,x1) == f1(y2, x2): {check_f1(y1, y2, x1, x2)}\n")


    # Case 2
    # *   Choose x1,y1,x2 arbitrarily (with x1 != x2) and let v := AES(y1,x1)
    #     Set y2 = AES^{-1}(x2, v ⊕ y1 ⊕ x2)
    x1 = os.urandom(16)     # key
    y1 = os.urandom(16)
    x2 = os.urandom(16)
    while x1 == x2:
        x2 = os.urandom(16)

    cipher =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher.encryptor()
    v = encryptor.update(y1) + encryptor.finalize()

    key = (int.from_bytes(v, byteorder='big') ^ int.from_bytes(y1, byteorder='big')
                ^ int.from_bytes(x2, byteorder='big')).to_bytes(16, byteorder='big')

    cipher2 = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
    decryptor = cipher2.decryptor()
    y2 = decryptor.update(x2) + decryptor.finalize()
    print(f"Case 2\n"
          f"f(y1,x1) == f1(y2, x2): {check_f1(y1, y2, x1, x2)}\n")


    # Case 3
    # *   Choose x1,y1,y2 arbitrarily (with y1 != y2) and let v := AES(y1,x1).
    #     Set x2 = AES^{-1}(y2, v ⊕ y1 ⊕ y2)
    x1 = os.urandom(16)     # key
    y1 = os.urandom(16)
    y2 = os.urandom(16)
    while y1 == y2:
        y2 = os.urandom(16)

    cipher =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher.encryptor()
    v = encryptor.update(y1) + encryptor.finalize()

    key = (int.from_bytes(v, byteorder='big') ^ int.from_bytes(y1, byteorder='big')
                ^ int.from_bytes(y2, byteorder='big'))\
        .to_bytes(16, byteorder='big')
    cipher2 = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
    decryptor = cipher2.decryptor()
    x2 = decryptor.update(y2) + decryptor.finalize()
    print(f"Case 3\n"
          f"f(y1,x1) == f1(y2, x2): {check_f1(y1, y2, x1, x2)}\n")

    # Case 4
    # Choose x1,y1,y2 arbitrarily (with y1 != y2) and let v := AES(y1,x1).
    #     Set x2 = AES^{-1}(y2, v ⊕ y2)
    x1 = os.urandom(16)     # key
    y1 = os.urandom(16)
    y2 = os.urandom(16)
    while y1 == y2:
        y2 = os.urandom(16)

    cipher =Cipher(algorithm=algorithms.AES(x1), mode=modes.ECB())
    encryptor = cipher.encryptor()
    v = encryptor.update(y1) + encryptor.finalize()

    key = (int.from_bytes(v, byteorder='big') ^ int.from_bytes(y2, byteorder='big'))\
        .to_bytes(16, byteorder='big')
    cipher2 = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
    decryptor = cipher2.decryptor()
    x2 = decryptor.update(y2) + decryptor.finalize()
    print(f"Case 4\n"
          f"f(y1,x1) == f1(y2, x2): {check_f1(y1, y2, x1, x2)}\n")