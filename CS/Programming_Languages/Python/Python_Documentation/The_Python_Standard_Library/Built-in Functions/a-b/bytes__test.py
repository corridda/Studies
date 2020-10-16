"""class bytes([source[, encoding[, errors]]])"""
# https://www.programiz.com/python-programming/methods/built-in/bytes

"""Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256.
'bytes' is an immutable version of 'bytearray' – it has the same non-mutating methods
and the same indexing and slicing behavior."""


def main():
    print(f"bytes(): {bytes()}")
    print(f"bytes(5): {bytes(5)}")
    print(f"bytes([0,1,2,3,4,5]): {bytes([0,1,2,3,4,5])}")
    print(f"bytes('Example of string', encoding='utf-8'): {bytes('Example of string', encoding='utf-8')}")

    bytes_obj = bytes('Example of string', encoding='utf-8')

    # TypeError: 'bytes' object is not callable
    try:
        bytes_obj += bytes_obj(' New string', encoding='utf-8')
    except TypeError as e:
        print(repr(e))

    # it's also immutable
    try:
        bytes_obj[-1] = ord('!')
    except TypeError as e:
        print(repr(e))


if __name__ == "__main__":
    main()