# Find the largest and smallest number in a list — first with max()/min(), then without them.

numbers = [2, 5, 8, 3, 12]

# Using max() and min()
largest = max(numbers)
smallest = min(numbers)
print(f"Largest using max(): {largest}")
print(f"Smallest using min(): {smallest}")

# Without using max() and min()
largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(f"Largest without using max(): {largest}")
print(f"Smallest without using min(): {smallest}")