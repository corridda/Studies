import sys

# The sys module also has attributes for stdin, stdout, and stderr.
# The latter is useful for emitting warnings and error messages to make them visible
# even when stdout has been redirected
print(sys.stderr.write('Warning, log file not found starting a new one\n'))

# The most direct way to terminate a script is to use sys.exit().
a = 10
if a == 10:
    try:
        sys.exit()
    finally:
        print("The programe was terminated.")
else:
    print("The programe wasn't terminated.")