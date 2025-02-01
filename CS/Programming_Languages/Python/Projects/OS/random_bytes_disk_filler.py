#! /usr/bin/env python3

"""Fill the disk `disk_letter` with files containing random bytes."""
__author__ = 'Igor Vasilev'

from secrets import token_bytes


def main():
    counter = 1
    file_size = 1024 * 1024 * 100
    disk_letter = "e"

    while file_size > 0:
        try:
            with open(f"{disk_letter}:/file_{counter}.bin", "wb") as f:
                f.write(token_bytes(file_size))
        except Exception:
            file_size //= 2
            continue
        counter += 1


if __name__ == '__main__':
    main()
