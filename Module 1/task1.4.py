# Ask the user for a price and quantity, then calculate the total bill.


price = float(input("Please enter the price per item: "))

quantity = int(input("Please enter the quantity: "))

total_bill = price * quantity

print(f"The total bill is: ${total_bill:.2f}")