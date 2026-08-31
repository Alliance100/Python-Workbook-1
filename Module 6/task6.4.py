#  Save a dictionary to a JSON file, then load it back and print it.
import json

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

data = {
    "name": name,
    "age": age,
    "city": city
}

# Save dictionary to JSON file
with open("data.json", "w") as f:
    json.dump(data, f)

# Load dictionary from JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)