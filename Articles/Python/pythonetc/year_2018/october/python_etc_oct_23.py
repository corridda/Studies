"""https://t.me/pythonetc/230"""

"""You can modify the code behavior during unit tests not only by using mocks and other advanced techniques
but also with straightforward object modification:"""

import random
import unittest
from unittest import TestCase

# class Foo:
#     def is_positive(self):
#         return self.rand() > 0
#
#     def rand(self):
#         return random.randint(-2, 2)
#
#
# class FooTestCase(TestCase):
#     def test_is_positive(self):
#         foo = Foo()
#         foo.rand = lambda: 1
#         self.assertTrue(foo.is_positive())
#
#
# if __name__ == '__main__':
#     unittest.main()


"""That's not gonna work if rand is property or any other descriptor.
In that case, you should modify the class, not the object.
However, modifying Foo might affect other tests, so the best way to deal with it is to create descendant."""

class Foo:
    def is_positive(self):
        return self.rand > 0

    @property
    def rand(self):
        return random.randint(-2, 2)


class FooTestCase(TestCase):
    def test_is_positive(self):
        class TestFoo(Foo):
            @property
            def rand(self):
                return 1
        foo = TestFoo()
        self.assertTrue(foo.is_positive())

if __name__ == '__main__':
    unittest.main()