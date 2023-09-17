"""vars([object])"""
# https://www.programiz.com/python-programming/methods/built-in/vars

from pprint import pprint

"""Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

Objects such as modules and instances have an updateable __dict__ attribute; however, other objects may have write
restrictions on their __dict__ attributes (for example, classes use a types.MappingProxyType
to prevent direct dictionary updates).

Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads
since updates to the locals dictionary are ignored.
"""

# Example: How vars() works?
class Foo:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b


InstanceOfFoo = Foo()
print(f"vars(InstanceOfFoo): {vars(InstanceOfFoo)}\n")


"""Also, run these statements on python shell:
>>> vars(list)
>>> vars(str)
>>> vars(dict)"""


pprint(vars(list))
print()
pprint(vars(str))
print()
pprint(vars(dict))