words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# There will be an attempt to create an infinite list, inserting 'defenestrate' over and over again.
# for w in words:
#     if len(w) > 6:
#         words.insert(0, w)
# print('words:', words)

"""
If you need to modify the sequence you are iterating over while inside the loop
(for example to duplicate selected items), it is recommended that you first make a copy.
Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:
"""
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print('words:', words)