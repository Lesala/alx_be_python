def perform_operation(num1, num2, operation):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        else:
            return "Error: Unsupported operation"
    except Exception as e:
        return f"Error: {str(e)}"
