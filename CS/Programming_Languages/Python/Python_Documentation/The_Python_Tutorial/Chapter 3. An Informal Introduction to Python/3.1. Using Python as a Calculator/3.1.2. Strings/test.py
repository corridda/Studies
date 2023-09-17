print('C:\some\name')  # here \n means newline!

# If you don’t want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote:
print(r'C:\some\name')  # note the r before the quote
print()

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print('un' * 3 + 'ium')  # 3 times 'un', followed by 'ium'

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other
# are automatically concatenated.
print('Py' 'thon')

# This feature is particularly useful when you want to break long strings.
# This only works with two literals though, not with variables or expressions.
print('Put several strings within parentheses '
      'to have them joined together.')

# f you want to concatenate variables or a variable and a literal, use +:
prefix = 'Py'
print(prefix + 'thon')

# Strings can be indexed (subscripted), with the first character having index 0.
word = 'python'
print(word[0] + word[1] + word[2] + word[3] + word[4] + word[5])

# Indices may also be negative numbers, to start counting from the right.
# Note that since -0 is the same as 0, negative indices start from -1.
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])

# In addition to indexing, slicing is also supported.
# While indexing is used to obtain individual characters, slicing allows you to obtain substring:
# [Note how the start is always included, and the end always excluded.]
print(word[0:2])    # characters from position 0 (included) to 2 (excluded)
print(word[2:5])    # characters from position 2 (included) to 5 (excluded)
print(word[:2] + word[2:])
print(word[:4] + word[4:])

# Slice indices have useful defaults; an omitted first index defaults to zero,
# an omitted second index defaults to the size of the string being sliced.
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # character from position 4 (included) to the end
print(word[-2:])   # characters from the second-last (included) to the end

# Attempting to use an index that is too large will result in an error:
try:
      print(word[42])   # the word only has 6 characters
except IndexError:
      print('IndexError: string index out of range')

# However, out of range slice indexes are handled gracefully when used for slicing:
print(word[4:42])
print(word[42:])

# python strings cannot be changed — they are immutable.
# Therefore, assigning to an indexed position in the string results in an error:
try:
      word[0] = 'J'
except TypeError:
      print("TypeError: 'str' object does not support item assig")

# If you need a different string, you should create a new one:
new_word = word[:]
print(new_word)
print('id(word):', id(word))
print('id(new_word):', id(new_word))
new_word +=  '_2'
print('new_word:', new_word)
print('id(word):', id(word))
print('id(new_word):', id(new_word))

# The built-in function len() returns the length of a string
s = 'supercalifragilisticexpialidocious'
print('len(s):', len(s))