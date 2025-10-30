class Calculator:
    """A simple calculator demonstrating class and static methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method that returns the sum of two numbers.
        It does not depend on class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method that returns the product of two numbers.
        It can access class-level data through 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
