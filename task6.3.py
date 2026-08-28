# Take a name from the user and append it to a file (like a contact list).

name = input("Enter a name: ")
with open("contacts.txt", "a") as f:
    f.write(name + "\n")