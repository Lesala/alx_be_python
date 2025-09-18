# Simple calculator that matches case for operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Prompting user to enter an operator
operator = input("Enter an operator (+, -, *, /): ")

# constructing a match-case statement to handle different operations
match operator:
    case "+":
        print("The result is ", num1 + num2)
    case "-":
        print("The result is ", num1 - num2)
    case "*":
        print("The result is ", num1 * num2)
    case "/":
        print("The result is ", num1 / num2)
    case _:
        print("Invalid operator")

