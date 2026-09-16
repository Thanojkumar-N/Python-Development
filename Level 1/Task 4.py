# Task 4: Calculator Program
# Create a Python program that acts as a simple calculator.

def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error! Division by zero."
        result = num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error! Modulo by zero."
        result = num1 % num2
    else:
        return "Invalid operator!"

    return f"Result: {result}"

if __name__ == "__main__":
    print(calculator())
