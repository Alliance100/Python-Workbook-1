# Use *args to build a function that totals any number of numbers passed to it.

def total_numbers(*args):
    return sum(args)

print(total_numbers(1, 2, 36, 41, 5))