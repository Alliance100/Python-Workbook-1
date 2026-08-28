# Write a function that takes a string and counts the vowels in it.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


text = input("Enter a sentence: ")

print(f"Number of vowels in '{text}': {count_vowels(text)}")