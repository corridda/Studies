#  The re module provides regular expression tools for advanced string processing

import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat hat'))


# When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:
print('tea for too'.replace('too', 'two'))