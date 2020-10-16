"""breakpoint(*args, **kws)"""
# https://realpython.com/python37-new-features/

# A breakpoint is a signal inside your code that execution should temporarily stop,
# so that you can look around at the current state of the program.

# the old implementation of a breakpoint
def divide_old(e, f):
    import pdb
    pdb.set_trace()
    return f / e

# the new implementation of a breakpoint
# In the background, breakpoint() is first importing pdb and then calling pdb.set_trace() for you.
def divide_new(e, f):
    breakpoint()
    return f / e

def main():
    # print(f"divide_old(0, 10): {divide_old(0, 10)}")
    print(f"divide_new(0, 10): {divide_new(0, 10)}")

if __name__ == "__main__":
    main()