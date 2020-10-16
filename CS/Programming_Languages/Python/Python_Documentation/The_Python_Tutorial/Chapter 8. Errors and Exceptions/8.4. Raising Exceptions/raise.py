# raise NameError('HiThere')

# If you need to determine whether an exception was raised but don’t intend to handle it:
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise