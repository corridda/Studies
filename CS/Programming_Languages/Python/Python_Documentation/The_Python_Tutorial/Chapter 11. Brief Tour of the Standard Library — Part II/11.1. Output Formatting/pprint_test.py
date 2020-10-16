import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
print("pprint.pprint(t, width=30):")
pprint.pprint(t, width=30)
print()

print("pprint.pprint(t):")
pprint.pprint(t)
print()

print("pprint.pprint(t, indent=5):")
pprint.pprint(t, indent=5)
print()

print("pprint.pprint(t, indent=2, compact=True):")
pprint.pprint(t, indent=2, compact=True)
