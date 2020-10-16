import os

print('os.cpu_count():', os.cpu_count())
print('os.getlogin():', os.getlogin())
print('os.getpid():', os.getpid())
print('os.listdir():', os.listdir('d:\\today'))
print('os.lstat():', os.lstat('d:\\today'))

os.remove('d:\\today\\2.txt')
os.rename('d:\\today\\1.txt', 'd:\\today\\1_1.txt')



