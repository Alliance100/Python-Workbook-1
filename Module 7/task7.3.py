# Use the math module to find a number's square root and factorial of input.

import math

number = int(input("Enter a number: "))

square_root = math.sqrt(number)
factorial = math.factorial(number)

print(f"Square root of {number}: {square_root}")
print(f"Factorial of {number}: {factorial}")