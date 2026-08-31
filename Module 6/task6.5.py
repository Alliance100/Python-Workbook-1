# Read a .txt file and show only the lines that contain a specific word.

word = input("Enter the word to search for: ")

with open("output.txt", "r") as f:
    for line in f:
        if word.lower() in line.lower():
            print(line.strip())