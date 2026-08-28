# Write a few lines to a text file, then read it back and display it on screen.

with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")

with open("output.txt", "r") as f:
    content = f.read()
    print(content)