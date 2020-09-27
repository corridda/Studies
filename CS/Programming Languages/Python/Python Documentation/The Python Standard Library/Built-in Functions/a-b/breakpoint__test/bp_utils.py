from pprint import pprint
import sys

def print_locals():
    caller = sys._getframe(1)  # Caller is 1 frame up.
    pprint(caller.f_locals)