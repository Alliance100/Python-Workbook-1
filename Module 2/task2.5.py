# Build a shopping cart that supports adding and removing items (using a list).

cart = []

item1 = input("Enter first item: ")
cart.append(item1)

item2 = input("Enter second item: ")
cart.append(item2)

item3 = input("Enter third item: ")
cart.append(item3)

print(f"Your cart: {cart}")
print(f"Total items: {len(cart)}")

remove = input("Which item do you want to remove? ")

cart.remove(remove)

print(f"Final cart: {cart}")