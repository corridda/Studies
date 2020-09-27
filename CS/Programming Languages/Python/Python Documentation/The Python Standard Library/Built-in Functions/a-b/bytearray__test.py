"""class bytearray([source[, encoding[, errors]]])"""
# https://www.programiz.com/python-programming/methods/built-in/bytearray

"""Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256."""


def main():
    print(f"bytearray(): {bytearray()}")
    print(f"bytearray(5): {bytearray(5)}")
    print(f"bytearray([0,1,2,3,4,5]): {bytearray([0,1,2,3,4,5])}\n")

    s = 'Python is interesting.'
    bytes_string = bytearray(s, encoding='utf-8')
    print(f"bytes_string: {bytes_string}")
    print(f"type(bytes_string[0]): {type(bytes_string[0])}")
    bytes_string[-1] = ord('!')
    print(f"bytes_string: {bytes_string}")

    # It has most of the usual methods of mutable sequences, described in Mutable Sequence Types
    bytes_string = bytearray([ord('*')]*3) + bytes_string + bytearray([ord('*')]*3)
    print(f"bytes_string: {bytes_string}\n")

    bytes = bytearray([0,1,2,3])
    print(f"bytes: {bytes}")
    print(f"type(bytes[0]): {type(bytes[0])}")
    bytes[0] = 16
    print(f"bytes: {bytes}\n")

    # contents must be only the integers in the range 0 <= x < 256
    try:
        bytes[0] = 256
        print(f"bytes: {bytes}")
    except ValueError as e:
        print(repr(e))


if __name__ == "__main__":
    main()
