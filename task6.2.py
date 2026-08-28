# Count how many lines and words are in a file.

with open("output.txt", "r") as f:
    content = f.read()
    lines = content.split('\n')
    words = content.split()
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")