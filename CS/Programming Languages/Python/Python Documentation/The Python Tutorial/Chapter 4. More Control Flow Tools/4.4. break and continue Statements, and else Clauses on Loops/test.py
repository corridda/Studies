# Here the else clause belongs to the for loop, not the if statement.)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
print()

# The continue statement, also borrowed from C, continues with the next iteration of the loop:
for i in range(2, 10):
    if i % 2 == 0:
        print("Found an even number", i)
        continue
    print("Found an odd number", i)