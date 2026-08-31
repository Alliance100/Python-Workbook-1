# Raise a custom error if an entered age is less than 0.

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print(f"Your age is: {age}")