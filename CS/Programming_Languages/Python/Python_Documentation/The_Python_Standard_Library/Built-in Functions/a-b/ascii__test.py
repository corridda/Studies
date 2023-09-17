"""ascii(object)"""
# https://www.programiz.com/python-programming/methods/built-in/ascii

"""As repr(), return a string containing a printable representation of an object,
but escape the non-ASCII characters in the string returned by repr() using \\x, \\u or \\U escapes."""

def main():
    normalText = 'python is interesting'
    print(ascii(normalText))

    otherText = 'Pythön is interesting'
    print(ascii(otherText))

    print('Pyth\xf6n is interesting\n')

    randomList = ['python', 'Pythön', 5]
    print(f"ascii(randomList): {ascii(randomList)}")
    print(f"repr(randomList): {repr(randomList)}")

if __name__ == "__main__":
    main()