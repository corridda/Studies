# The with statement allows objects like files to be used in a way
# that ensures they are always cleaned up promptly and correctly.
# After the statement is executed, the file f is always closed,
# even if a problem was encountered while processing the lines.

with open('file.txt', 'r') as f:
    for line in f:
        print(line, end='')

