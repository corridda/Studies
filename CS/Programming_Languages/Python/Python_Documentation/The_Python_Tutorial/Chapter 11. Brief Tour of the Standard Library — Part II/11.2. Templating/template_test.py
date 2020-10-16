from string import Template

t = Template('${village}folk send $$10 to $cause.')
print(t)
print(t.substitute(village='Nottingham', cause='the ditch fund'))

# The substitute() method raises a KeyError when a placeholder
# is not supplied in a dictionary or a keyword argument.
try:
    print(t.substitute(village='Nottingham', caaause='the ditch fund'))
except KeyError as e:
    print(repr(e))

# For mail-merge style applications, user supplied data may be incomplete
# and the safe_substitute() method may be more appropriate —
# it will leave placeholders unchanged if data is missing:
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')

try:
    t.substitute(d)
except KeyError as e:
    print(repr(e))

print(t.safe_substitute(d))