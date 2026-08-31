# Build a calculator that doesn't crash on divide-by-zero, but shows a message instead .

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = divide(num1, num2)

print(f"Result: {result}")