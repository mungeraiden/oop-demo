class Point:
    """
    Docstring for Point
    """
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x
    
    def set_x(self, new_x: float) -> None:
        self._x = new_x

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"
    
class Circle:
    """
    Docstring for Circle
    """
    def __init__(self, radius: float = 1.0, center: Point = None) -> None:
        self._radius = radius
        if center is None:
            center = Point()
        self._center = center

    def __str__(self):
        return f"{self._center}"
    

origin = Point()
print(origin)
p1 = Point(-2.4, 1.8)
print(p1)

unit_circle = Circle()
print(unit_circle)
c1 = Circle(5.0, p1)