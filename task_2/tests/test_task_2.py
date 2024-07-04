from task_2.task_2 import Point, Circle, is_belongs, PointPosition


def test_point_inside_circle():
    center = Point(0, 0)
    circle = Circle(center, 10)
    point_inside = Point(0, 5)
    assert is_belongs(circle, point_inside) == PointPosition.IN


def test_point_outside_circle():
    center = Point(0, 0)
    circle = Circle(center, 10)
    point_outside = Point(15, 15)
    assert is_belongs(circle, point_outside) == PointPosition.OUT


def test_point_on_circle():
    center = Point(0, 0)
    circle = Circle(center, 10)
    point_on_circle = Point(10, 0)
    assert is_belongs(circle, point_on_circle) == PointPosition.ON
