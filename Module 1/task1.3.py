# Make a simple calculator that takes two numbers and prints the result of +, -, ×, ÷.

num1 = float(input("Please enter the first number: "))

num2 = float(input("Please enter the second number: "))


print(f"{num1} + {num2} = {num1 + num2}")

print(f"{num1} - {num2} = {num1 - num2}")

print(f"{num1} × {num2} = {num1 * num2}")

print(f"{num1} ÷ {num2} = {num1 / num2 if num2 != 0 else 'Error: Division by zero is not allowed.'}")