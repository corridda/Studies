"""compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)"""
# https://www.programiz.com/python-programming/methods/built-in/compile


"""Compile the 'source' into a code or AST object. Code objects can be executed by exec() or eval().
'source' can either be a normal string, a byte string, or an AST object."""


"""Here, the source is in normal string form. The filename is 'sumstring'.
And, the exec mode later allows the use of exec() method.
The compile() method converts the string to python code object.
The code object is then executed using exec() method."""

def main():
    codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
    codeObejct = compile(codeInString, 'sumstring', 'exec')
    exec(codeObejct)


if __name__ == "__main__":
    main()