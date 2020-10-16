"""EXERCISE 3.14. PARALLEL COUNTER MODE

Extend your counter mode implementation to use a thread pool to generate the key stream in
parallel. Remember that to generate a block of key stream, all that is required is the starting IV
and which block of key stream is being generated (e.g., 0 for the first 16-byte block, 1 for the
second 16-byte block, etc.). Start by creating a function that can generate any particular block
of key stream, perhaps something like keystream(IV, i). Next, parallelize the generation
of a key stream up to n by dividing the counter sequence among independent processes any
way you please, and have them all work on generating their key stream blocks independently.
"""