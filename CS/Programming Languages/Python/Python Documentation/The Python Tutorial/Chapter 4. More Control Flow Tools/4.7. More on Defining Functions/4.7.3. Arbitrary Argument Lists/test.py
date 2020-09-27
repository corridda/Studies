import tempfile

# Before the variable number of arguments, zero or more normal arguments may occur.
def write_multiple_items(separator, *args):
    with tempfile.TemporaryFile() as f:
        f.write(separator.join(args))
        f.seek(0)
        print(f.read())

write_multiple_items(b" ", b'A', b'string', b'to', b'write')


# Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
