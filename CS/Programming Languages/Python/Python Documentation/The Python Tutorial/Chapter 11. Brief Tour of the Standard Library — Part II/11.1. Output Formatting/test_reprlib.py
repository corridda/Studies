"""Redo the builtin repr() (representation) but with limits on most sizes."""

import reprlib

print(set('supercalifragilisticexpialidocious'))
print(type(set('supercalifragilisticexpialidocious')), '\n')

print(reprlib.repr(set('supercalifragilisticexpialidocious')))
print(type(reprlib.repr(set('supercalifragilisticexpialidocious'))))
