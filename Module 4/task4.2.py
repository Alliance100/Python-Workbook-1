# Write a function that returns both the sum and average of a list.
def sum_and_average(lst):
    total = sum(lst)
    average = total / len(lst) if lst else 0
    return total, average

# Example usage:
numbers = [17, 24, 31, 44, 55]
total, average = sum_and_average(numbers)
print(f"Sum: {total}, Average: {average}")