# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match case
match operation:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("Invalid operation selected.")

