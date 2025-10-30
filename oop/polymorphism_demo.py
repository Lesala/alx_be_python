import math

class Shape:
    """Base class for all shapes."""
    def area(self) -> float:
        """Method to calculate area — must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length: float, width: float):
        self.length: float = length
        self.width: float = width

    def area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
