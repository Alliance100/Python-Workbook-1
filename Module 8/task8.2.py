# Ask the user for a number — if they type text, ask again (handle ValueError).

while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(f"You entered: {num}")