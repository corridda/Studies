"""print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)"""
# https://www.programiz.com/python-programming/methods/built-in/print

"""Print objects to the text stream file, separated by 'sep' and followed by 'end'. 'sep', 'end', 'file' and 'flush',
if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like str() does and written to the stream,
separated by 'sep' and followed by 'end'. Both 'sep' and 'end' must be strings; they can also be None,
which means to use the default values. If no objects are given, print() will just write 'end'.

The 'file' argument must be an object with a write(string) method; if it is not present or None,
sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used
with binary mode file objects. For these, use file.write(...) instead.

Whether output is buffered is usually determined by 'file', but if the 'flush' keyword argument is true,
the stream is forcibly flushed.
"""


# Example 1: How print() works in python?

print("python is fun.")

a = 5
# Two objects are passed
print("a =", a)

b = a
# Three objects are passed
print('a =', a, '= b')
print()

"""In the above program, only objects parameter is passed to print() function (in all three print statements).
Hence, ' ' separator is used. Notice, the space between two objects in output.
'end' parameter '\n' (newline character) is used. Notice, each print statement displays the output in the new line.
'file' is sys.stdout. The output is printed on the screen.
'flush' is False. The stream is not forcibly flushed."""



# Example 2: print() with separator and end parameters

a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')
print()



# Example 3: print() with file parameter

# In python, you can print objects to the file by specifying the file parameter.
sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()

"""This program tries to open the python.txt in writing mode. If this file doesn't exist,
python.txt file is created and opened in writing mode.

Here, we have passed sourceFile file object to the file parameter.
The string object 'Pretty cool, huh!' is printed to python.txt file (check it in your system).

Finally, the file is closed using close() method."""