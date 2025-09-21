# Simple Calculator using match-case

# Input operator
op = input("Enter an operator (+, -, *, /): ")

# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Match-case (similar to switch in C)
match op:
    case '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    case '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    case '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    case '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero is not allowed.")
    case _:
        print("Invalid operator.")