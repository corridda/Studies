"""The library also offers other tools such as the bisect module
with functions for manipulating sorted lists:"""

import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
print(f"type(bisect.insort(scores, (300, 'ruby'))): {type(bisect.insort(scores, (300, 'ruby')))}")
print(f'scores: {scores}\n')

bisect.insort(scores, (300, 'ruby'))
print(f'scores: {scores}')
print(f'bisect.bisect(scores, (300, "ruby")): {bisect.bisect(scores, (300, "ruby"))}')
print(f'scores: {scores}')
