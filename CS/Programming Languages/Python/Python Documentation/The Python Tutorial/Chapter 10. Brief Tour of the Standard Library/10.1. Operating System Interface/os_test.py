# The os module provides dozens of functions for interacting with the operating system

import os

# os.getcwd() [return the current working directory]
print(os.getcwd())

# os.chdir(the specified path) [Change the current working directory to the specified path]
os.chdir('d:\\')
print(os.getcwd())

# os.system() [Run the command (mkdir [Create a directory] in this case) in the system shell]
os.system('mkdir today')


# The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:
# dir(os) # [returns a list of all module functions]
# help(os) [returns an extensive manual page created from the module's docstrings]


# For daily file and directory management tasks, the shutil module provides
# a higher level interface that is easier to use:

import shutil

# shutil.copyfile(src, dst, ...) [Copy data from src to dst]
os.chdir('d:\\today')
print(os.getcwd())
with open('1.txt', 'w') as f:
    f.write('12345\n')
shutil.copyfile('1.txt', '2.txt')

# shutil.move(src, dst, ...) [Recursively move a file or directory to another location.]
shutil.move('1.txt', 'd:\\')
shutil.move('d:\\1.txt', 'd:\\today')