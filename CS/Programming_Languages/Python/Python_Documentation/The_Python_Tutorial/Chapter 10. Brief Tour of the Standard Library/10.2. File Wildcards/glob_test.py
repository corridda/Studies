# The glob module provides a function for making file lists from directory wildcard searches.

import glob
import os

# glob.glob(pathname,  *, ...) [Return a list of paths matching a pathname pattern.]
print("glob.glob('*.py')", glob.glob('*.py'))

os.chdir("d:\\Фото\\Наша семья\\2017\\09_(03.12.2017 - Ботанический сад)\\")
print(os.getcwd(), '\n\nContents of "d:\\Фото\\Наша семья\\2017\\09_(03.12.2017 - Ботанический сад)\\":')
for f in glob.glob("*.*"):
    print(f)
