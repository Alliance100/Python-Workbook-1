# Try to open a file that doesn't exist and handle the error gracefully.
import os

file_name = input("Enter the file name: ")
folder = os.path.dirname(__file__)

try:
    with open(f"{folder}/{file_name}", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: The file does not exist.")