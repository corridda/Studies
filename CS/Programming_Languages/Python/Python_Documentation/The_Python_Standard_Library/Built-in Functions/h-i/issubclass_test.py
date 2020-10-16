"""issubclass(class, classinfo)"""
# https://www.programiz.com/python-programming/methods/built-in/issubclass

"""Return true if class is a subclass (direct, indirect or virtual) of classinfo.
A class is considered a subclass of itself. classinfo may be a tuple of class objects,
in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised."""

# Example: How issubclass() works?
class Polygon:
    def __init__(polygonType):
        print('Polygon is a', polygonType)


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')


print(f"issubclass(Triangle, Polygon): {issubclass(Triangle, Polygon)}")
print(f"issubclass(Triangle, list): {issubclass(Triangle, list)}")
print(f"issubclass(Triangle, (list, Polygon)): {issubclass(Triangle, (list, Polygon))}")
print(f"issubclass(Polygon, (list, Polygon)): {issubclass(Polygon, (list, Polygon))}")
