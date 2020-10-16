"""callable(object)"""
# https://www.programiz.com/python-programming/methods/built-in/callable

"""Return True if the object argument appears callable, False if not.
If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed."""


class Foo:
    def __call__(self):
        print('Print Something')


class Bar:
    def printLine(self):
        print('Print Something')


def main():
    print(f"callable(callable): {callable(callable)}")
    print(f"callable(int): {callable(int)}")
    print(f"callable(int()): {callable(int())}")
    print(f"callable(None): {callable(None)}")
    print(f"callable([]): {callable([])}")
    print(f"callable(list): {callable(list)}\n")

    x = 5
    print(f"callable(x): {callable(x)}")

    def testFunction():
        print("Test")

    print(f"callable(testFunction): {callable(testFunction)}\n")

    # The instance of Foo class appears to be callable (and is callable in this case).
    print(f"callable(Foo): {callable(Foo)}")
    InstanceOfFoo = Foo()
    # Prints 'Print Something'
    InstanceOfFoo()
    print()

    # Object Appears to be Callable but isn't callable.
    print(f"callable(Bar): {callable(Bar)}")

    # The instance of Bar class appears to be callable but it's not callable. The following code will raise an error.
    InstanceOfBar = Bar()

    # Raises an Error
    # 'Bar' object is not callable
    try:
        InstanceOfBar()
    except TypeError as e:
        print(repr(e))


if __name__ == "__main__":
    main()
