"""class bool([x])"""

"""Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure.
If x is false or omitted, this returns False; otherwise it returns True."""

class BoolReturnFalse:
    def __bool__(self):
        return False

class LenReturnZero:
    def __len__(self):
        return False

def main():
    print(f"bool(3): {bool(3)}")
    print(f"bool(False): {bool(False)}")
    print(f"bool(None): {bool(None)}")
    print(f"bool([]): {bool([])}")
    print(f"bool([0]): {bool([0])}")
    print(f"bool(set()): {bool(set())}")
    print(f"bool({{}}): {bool({})}")
    print(f"bool({0j}): {bool(0j)}")
    print(f"bool(10): {bool(10)}")
    print(f"bool((1,2,3)): {bool((1,2,3))}\n")

    """By default, an object is considered true unless its class defines either a __bool__() method
    that returns False or a __len__() method that returns zero, when called with the object. """
    print(f"bool(BoolReturnFalse()): {bool(BoolReturnFalse())}")
    print(f"bool(LenReturnZero()): {bool(LenReturnZero())}")


if __name__ == "__main__":
    main()