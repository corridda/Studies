from dataclasses import dataclass
from math import sqrt

"""Переопределение и перегрузка"""


@dataclass()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def init_from_one_coordinate(cls, coordinate):
        return cls(coordinate, coordinate)


@dataclass()
class Quadrilateral:
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self) -> float:
        a = sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        b = sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)
        c = sqrt((self.p4.x - self.p3.x) ** 2 + (self.p4.y - self.p3.y) ** 2)
        d = sqrt((self.p4.x - self.p1.x) ** 2 + (self.p4.y - self.p1.y) ** 2)
        p = (a + b + c + d) / 2
        return sqrt((p - a) * (p - b) * (p - c) * (p - d))


def quadrilateral_area(*args):
    if len(args) == 4:
        quadrilateral = Quadrilateral(*args)
    elif len(args) == 1:
        quadrilateral = args[0]
    else:
        raise TypeError()

    return quadrilateral.area()


def main():
    p = Point.init_from_one_coordinate(5)
    print(f"p.x: {p.x}")
    print(f"p.y: {p.y}")

    print(f"quadrilateral_area(Point(0, 0), Point(0, 5), Point(5, 5), Point(5, 0)) = "
          f"{quadrilateral_area(Point(0, 0), Point(0, 5), Point(5, 5), Point(5, 0))}")
    print(f"quadrilateral_area(Quadrilateral(Point(0, 0), Point(0, 5), Point(7, 5), Point(7, 0))) = "
          f"{quadrilateral_area(Quadrilateral(Point(0, 0), Point(0, 5), Point(7, 5), Point(7, 0)))}")


if __name__ == '__main__':
    main()
