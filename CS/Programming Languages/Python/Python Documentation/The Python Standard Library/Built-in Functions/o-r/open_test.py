"""open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)"""
# https://www.programiz.com/python-programming/methods/built-in/open

"""Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised."""

# Example 1: How to open a file in Python?
# opens test.text file of the current directory
with open("test.txt") as f:
    print(f"{f.read()}")

# specifying full path
with open("c:/Users/Игорь/PycharmProjects/Books/Documentation/"
          "The Python Standard Library/2. Built-in Functions/o-r/test2.txt") as f:
    print(f"{f.read()}\n")

"""Since the mode is omitted, the file is opened in 'r' mode; opens for reading."""


# Example 2: Providing mode to open()
# opens for read
with open("c:/Users/Игорь/PycharmProjects/Books/Documentation/"
          "The Python Standard Library/2. Built-in Functions/o-r/test2.txt", mode='r') as f:
    print(f"{f.read()}\n")

# opens for write
with open("c:/Users/Игорь/PycharmProjects/Books/Documentation/"
          "The Python Standard Library/2. Built-in Functions/o-r/test3.txt", mode = 'w') as f:
    f.write("string\n")


# opens for writing to the end
with open("c:/Users/Игорь/PycharmProjects/Books/Documentation/"
          "The Python Standard Library/2. Built-in Functions/o-r/test3.txt", mode = 'a') as f:
    f.write("new string\n")

"""Python has a encoding system which is platform dependent.
Hence, it's recommended to specify the encoding type if you are working in a text mode."""
with open("c:/Users/Игорь/PycharmProjects/Books/Documentation/"
          "The Python Standard Library/2. Built-in Functions/o-r/test2.txt", mode='r', encoding='utf-8') as f:
    print(f"{f.read()}\n")