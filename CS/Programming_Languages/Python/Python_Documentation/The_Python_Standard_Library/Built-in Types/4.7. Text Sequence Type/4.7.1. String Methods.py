"""String Methods"""


# str.capitalize()
print(str.capitalize("the string with its first character capitalized."), '\n')


# str.casefold()
"""Casefolding is similar to lowercasing but more aggressive because it is intended to remove
all case distinctions in a string."""
print(str.casefold("The casefolding algorithm is described in section 3.13 of the Unicode Standard."), '\n')


# str.center(width[, fillchar])
print(str.center("String to center.", 30, '*'), '\n')


# str.count(sub[, start[, end]])
print(f"str.count('abc-dvd-abc-vdv-abc-dvd', 'abc'): {str.count('abc-dvd-abc-vdv-abc-dvd', 'abc')}\n")


# str.encode(encoding="utf-8", errors="strict")
print(str.encode('String to be encoded.', encoding='utf8', errors='ignore'), '\n')


# str.endswith(suffix[, start[, end]])
print(f"str.endswith('abc-dvd-abc-vdv-abc-dvd', 'abc'): {str.endswith('abc-dvd-abc-vdv-abc-dvd', 'abc')}")
print(f"str.endswith('abc-dvd-abc-vdv-abc-dvd', ('ab', 'vd')): "
      f"{str.endswith('abc-dvd-abc-vdv-abc-dvd', ('ab', 'vd'))}\n")


# str.expandtabs(tabsize=8)
print('unit_01\t012\t0123\t01234'.expandtabs())
print('unit_01\t012\t0123\t01234'.expandtabs(4), '\n')


# str.find(sub[, start[, end]])
"""Note:
 The find() method should be used only if you need to know the position of sub.
 To check if sub is a substring or not, use the in operator:"""
print(f"'Py' in 'python': {'Py' in 'python'}")
print(f"str.find('abc-dvd-abc-vdv-abc-dvd', 'vdv'): {str.find('abc-dvd-abc-vdv-abc-dvd', 'vdv')}")
print(f"str.find('abc-dvd-abc-vdv-abc-dvd', 'abs'): {str.find('abc-dvd-abc-vdv-abc-dvd', 'abs')}\n")


# str.format(*args, **kwargs)
"""Returns a copy of the string where each replacement field is replaced with the string value
of the corresponding argument."""
print("The sum of 1 + 2 is {0}".format(1+2), '\n')


# str.format_map(mapping)
class Default(dict):
    def __missing__(self, key):
        return key

print('{name} was born in {country}'.format_map(Default(name='Guido', country='Netherlands')))


# str.index(sub[, start[, end]])
"""Like find(), but raise ValueError when the substring is not found."""
try:
    print(f"str.index('abc-dvd-abc-vdv-abc-dvd', 'vdv'): {str.index('abc-dvd-abc-vdv-abc-dvd', 'vdv')}")
    print(f"str.index('abc-dvd-abc-vdv-abc-dvd', 'dfd'): {str.index('abc-dvd-abc-vdv-abc-dvd', 'dfd')}")
except ValueError as e:
    print(repr(e))
print()


# str.isalnum()
print(f"str.isalnum('ab12': {str.isalnum('ab12')}")
print(f"str.isalnum('**ab12**': {str.isalnum('**ab12**')}\n")


# str.isalpha()
print(f"str.isalpha(): {str.isalpha('')}")
print(f"str.isalpha('string'): {str.isalpha('string')}")
print(f"str.isalpha('ab12'): {str.isalpha('ab12')}\n")


# str.isascii()
print(f"str.isascii(''): {str.isascii('')}")
print(f"str.isascii('ab12'): {str.isascii('ab12')}")
print(f"str.isascii('Строка на русском'): {str.isascii('Строка на русском')}\n")


# str.isdecimal()
print(f"str.isdecimal('10'): {str.isdecimal('10')}")
print(f"str.isdecimal('10.5'): {str.isdecimal('10.5')}")
print(f"str.isdecimal('00'): {str.isdecimal('00')}")
ch1 = '\U00010A40'  # KHAROSHTHI DIGIT ONE
print(f"ch1 (KHAROSHTHI DIGIT ONE): {ch1}")
print(f"str.isdecimal('ch1'): {str.isdecimal(ch1)}\n")


# str.isdigit()
print(f"str.isdigit(''): {str.isdigit('')}")
print(f"str.isdigit('123'): {str.isdigit('123')}")
print(f"str.isdigit('*123*'): {str.isdigit('*123*')}")
print(f"ch1 (KHAROSHTHI DIGIT ONE): {ch1}")
print(f"str.isdigit('ch1'): {str.isdigit(ch1)}\n")


# str.isidentifier()
print(f"str.isidentifier('_abc'): {str.isidentifier('_abc')}")
print(f"str.isidentifier('abc'): {str.isidentifier('abc')}")
print(f"str.isidentifier('abc123'): {str.isidentifier('abc123')}")
print(f"str.isidentifier('123abc'): {str.isidentifier('123abc')}\n")


# str.islower()
print(f"str.islower(''): {str.islower('')}")
print(f"str.islower('abc'): {str.islower('abc')}")
print(f"str.islower('ABC'): {str.islower('ABC')}\n")


# str.isnumeric()
print(f"str.isnumeric(''): {str.isnumeric('')}")
print(f"str.isnumeric('10.5'): {str.isnumeric('10.5')}")
print(f"str.isnumeric('10'): {str.isnumeric('10')}")
ch2 = '\u2155'  # VULGAR FRACTION ONE FIFTH
print(f"ch2 (VULGAR FRACTION ONE FIFTH): {ch2}")
print(f"str.isnumeric(ch2): {str.isnumeric(ch2)}\n")


# str.isprintable()
print(f"str.isprintable(''): {str.isprintable('')}")
print(f"str.isprintable('abc123'): {str.isprintable('abc123')}")
str1 = '\n\t\n\r'
print(f"str.isprintable(str1): {str.isprintable(str1)}\n")


# str.isspace()
print(f"str.isspace(''): {str.isspace('')}")
print(f"str.isspace(' '): {str.isspace(' ')}")
tab = '\t'
print(f"str.isspace(tab): {str.isspace(tab)}\n")


# str.istitle()
print(f"str.istitle('This Is A Title'): {str.istitle('This Is A Title')}")
print(f"str.istitle('This Is not a Title'): {str.istitle('This Is not a Title')}\n")


# str.isupper()
print(f"str.isupper('abc'): {str.isupper('abc')}")
print(f"str.isupper('ABC'): {str.isupper('ABC')}\n")


# str.join(iterable)
print(f"' '.join(['first', 'second', 'third']): {' '.join(['first', 'second', 'third'])}")
try:
    print(f"' '.join([1,2,3]): {' '.join([1,2,3])}")
except TypeError as e:
    print(repr(e))
print()


# str.ljust(width[, fillchar])
print(f"{str.ljust('left justified string', 30, '*')}\n")


# str.lower()
print(f"str.lower('STRING TO BE LOWERCASED'): {str.lower('STRING TO BE LOWERCASED')}\n")


# str.lstrip([chars])
str2 = '  \t string to be left stripped'
print(f"{str.lstrip(str2)}")
print(f"'www.example.com'.lstrip('cmowz.'): {'www.example.com'.lstrip('cmowz.')}\n")


# str.partition(sep)
print(f"{str.partition('abc-dvd-abc-vdv-abc-dvd', '-vdv-')}")
print(f"{str.partition('abc-dvd-abc-vdv-abc-dvd', 'some_sep')}\n")


# str.replace(old, new[, count])
print(f"str.replace('abc-dvd-abc-vdv-abc-dvd', 'abc', 'cba'): "
      f"{str.replace('abc-dvd-abc-vdv-abc-dvd', 'abc', 'cba')}\n")


# str.rfind(sub[, start[, end]])
print(f"str.rfind('abc-dvd-abc-vdv-abc-dvd', 'dvd'): {str.rfind('abc-dvd-abc-vdv-abc-dvd', 'dvd')}")
print(f"str.rfind('abc-dvd-abc-vdv-abc-dvd', 'abs'): {str.rfind('abc-dvd-abc-vdv-abc-dvd', 'abs')}\n")


# str.rindex(sub[, start[, end]])
print(f"str.rindex('abc-dvd-abc-vdv-abc-dvd', 'dvd'): {str.rindex('abc-dvd-abc-vdv-abc-dvd', 'dvd')}")
try:
    print(f"{str.rindex('abc-dvd-abc-vdv-abc-dvd', 'abs')}")
except ValueError as e:
    print(repr(e))
print()


# str.rjust(width[, fillchar])
print(f"{str.rjust('string to be right justified', 50, '*')}\n")


# str.rpartition(sep)
print(f"{str.rpartition('abc-dvd-abc-vdv-abc-dvd', '-abc-')}\n")


# str.rsplit(sep=None, maxsplit=-1)
print(f"{str.rsplit('string to be splitted from the right side', maxsplit=3)}")
print(f"{str.rsplit('string to be splitted from the right side')}\n")


# str.rstrip([chars])
str3 = '\t \t string to be stripeed from the right side\t \t'
print(f"str.rstrip(str3): '{str.rstrip(str3)}'\n")


# str.split(sep=None, maxsplit=-1)
print(f"{str.split('string to be splitted from the left side', maxsplit=3)}")
print(f"{str.split('string to be splitted from the left side')}")
print(f"'1,2,,3,'.split(','): {'1,2,,3,'.split(',')}")
# If sep is not specified or is None, a different splitting algorithm is applied
print(f"'1 2 3'.split(): {'1 2 3'.split()}")
print(f"'1 2 3'.split(maxsplit=1): {'1 2 3'.split(maxsplit=1)}")
print(f"'   1   2   3   '.split(): {'   1   2   3   '.split()}\n")


# str.splitlines([keepends])
str4 = 'ab c\n\nde fg\rkl\r\n'
print(f"str4.splitlines(): {str4.splitlines()}")
print(f"str4.splitlines(keepends=True): {str4.splitlines(keepends=True)}")
print(f'"".splitlines(): {"".splitlines()}')
str5 = "One line\n"
print(f'str5.splitlines(): {str5.splitlines()}')
# For comparison, split('\n') gives:
print(''.split('\n'))
print('Two lines\n'.split('\n'), '\n')


# str.startswith(prefix[, start[, end]])
print(f"str.startswith('abc-dvd-abc-vdv-abc-dvd', 'abc'): {str.startswith('abc-dvd-abc-vdv-abc-dvd', 'abc')}")
print(f"str.startswith('abc-dvd-abc-vdv-abc-dvd', ('ab', 'vd')): "
      f"{str.startswith('abc-dvd-abc-vdv-abc-dvd', ('ab', 'vd'))}\n")


# str.strip([chars])
print(f"'   spacious   '.strip(): {'   spacious   '.strip()}")
print(f"'www.example.com'.strip('cmowz.'): {'www.example.com'.strip('cmowz.')}")
comment_string = '#....... Section 3.2.1 Issue #32 .......'
print(f"comment_string: {comment_string}")
print(f"comment_string.strip('.#! '): {comment_string.strip('.#! ')}\n")


# str.swapcase()
print(f"str.swapcase('string TO BE swapcased'): {str.swapcase('string TO BE swapcased')}\n")


# str.title()
print(f"'Hello world'.title(): {'Hello world'.title()}")
# A workaround for apostrophes can be constructed using regular expressions.
str6 = "they're bill's friends from the UK"
print(f"str6: {str6}")
print(f"str6.title(): {str6.title()}\n")


# str.upper()
print(f"str.upper('string to be uppercased'): {str.upper('string to be uppercased')}\n")


# str.zfill(width)
print(f"'42'.zfill(5): {'42'.zfill(5)}")
print(f"'-42'.zfill(5): {'-42'.zfill(5)}\n")
