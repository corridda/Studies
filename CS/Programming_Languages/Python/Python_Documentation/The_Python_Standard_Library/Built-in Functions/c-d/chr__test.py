"""chr(i)"""
# https://www.programiz.com/python-programming/methods/built-in/chr

"""Return the string representing a character whose Unicode code point is the integer i.
For example, chr(97) returns the string 'a', while chr(8364) returns the string 'Ђ'. This is the inverse of ord()."""


def main():
    print(f"chr(97): {chr(97)}")
    print(f"chr(8364): {chr(8364)}")
    print(f"chr(65): {chr(65)}")
    print(f"chr(1200): {chr(1200)}\n")

    # The valid range of the integer 'i' is from 0 through 1,114,111.
    # When you run the program, ValueError is raised.
    # It's because the argument passed to the chr() method is out of the range.
    try:
        print(chr(-1))
    except ValueError as e:
        print(repr(e))


if __name__ == "__main__":
    main()
