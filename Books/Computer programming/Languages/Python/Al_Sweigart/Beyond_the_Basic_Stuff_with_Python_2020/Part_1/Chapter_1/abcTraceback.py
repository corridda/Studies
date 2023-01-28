#!usr/bin/env python3

def a():
    print('Start of a()')
    b()  # Call b().

def b():
    print('Start of b()')
    c()  # Call c().

def c():
    print('Start of c()')
    42 / 0  # This will cause a zero divide error.

def main():
    a()

if __name__ == '__main__':
    main()