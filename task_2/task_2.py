import argparse
import math
from enum import IntEnum
from pathlib import Path


class PointPosition(IntEnum):
    ON = 0  # точка лежит на окружности
    IN = 1  # точка внутри
    OUT = 2  # точка снаружи


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, c: Point, r: int):
        self.c = c
        self.r = r


def is_belongs(circle: Circle, point: Point):
    delta_x = (point.x - circle.c.x) ** 2
    delta_y = (point.y - circle.c.y) ** 2
    dist = int(math.sqrt(delta_x + delta_y))

    if dist > circle.r:
        return PointPosition.OUT
    elif dist < circle.r:
        return PointPosition.IN
    elif dist == circle.r:
        return PointPosition.ON


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Задача №2")
    parser.add_argument("-p", help="", type=str, default="points.txt")
    parser.add_argument("-c", help="", type=str, default="circle.txt")
    parser.add_argument("-v", help="Детальный вывод", action="store_true")
    args = parser.parse_args()

    with open(Path(args.c), "r") as file:
        data = file.readline()
        x_, y_ = data.split(" ")
        x_, y_ = int(x_), int(y_)
        r_ = file.readline()
        r_ = int(r_)

    circle_ = Circle(Point(x_, y_), r_)

    points = list()
    with open(Path(args.p), "r") as file:
        for data in file:
            x_, y_ = data.split(" ")
            x_, y_ = int(x_), int(y_)
            points.append(Point(x_, y_))

    for point_ in points:
        position = is_belongs(circle_, point_)
        if args.v:
            print(f"Точка ({point_.x}, {point_.y}), находится {position}")
        else:
            print(position.value)
