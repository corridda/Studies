"""memoryview(obj)"""
# https://www.programiz.com/python-programming/methods/built-in/memoryview

"""Return a “memory view” object created from the given argument. 'obj' must support buffer protocol
(bytes, bytearray).
See Memory Views for more information."""



# Example 1: How memoryview() works in Python?

#random bytearray
randomByteArray = bytearray('ABC', 'utf-8')
mv = memoryview(randomByteArray)

# access memory view's zeroth index
print(f"mv[0]: {mv[0]}")

# create byte from memory view
print(f"bytes(mv[0:2]): {bytes(mv[0:2])}")

# create list from memory view
print(f"list(mv[0:3]): {list(mv[0:3])}\n")

"""Here, we created a memory view object mv from the byte array randomByteArray.
Then, we accessed the mv's 0th index 'A' and printed it (which gives the ASCII value - 65).
Again, we accessed the mv's indices from 0 and 1 ('AB') and converted them into bytes.
Finally, we accessed all indices of mv and converted it to a list.
Since, internally bytearray stores ASCII value for the alphabets,
the output is a list of ASCII values of A, B and C."""



# Example 2: Modify internal data using memory view

#random bytearray
randomByteArray = bytearray('ABC', 'utf-8')
print('Before updation:', randomByteArray)

mv = memoryview(randomByteArray)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', randomByteArray)

"""Here, we updated the memory view's 1st index to ASCII - 90 (Z).
Since, the memory view object mv references the same buffer/memory,
updating the index in mv also updates randomByteArray."""
