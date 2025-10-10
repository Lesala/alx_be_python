# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely performs division between numerator and denominator.
    Handles:
    - Non-numeric inputs
    - Division by zero
    Returns a user-friendly message.
    """
    try:
        # Attempt to convert both inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        # Handles invalid numeric conversion
        return "Error: Please provide numeric values only."

    except ZeroDivisionError:
        # Handles division by zero
        return "Error: You cannot divide by zero."
    