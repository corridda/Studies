import math

print(.1 + .1 + .1 == .3)                                           # False
print(round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1))   # False
print(round(.1 + .1 + .1, 1) == 0.3)                                # True
print()

# The math.fsum() function helps mitigate loss-of-precision during summation.
print(sum([0.1] * 10) == 1.0)       # False
print(math.fsum([0.1] * 10) == 1.0) # True

