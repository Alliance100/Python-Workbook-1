# Use a default argument: greet(name, lang="urdu") that greets based on the language.

def greet(name, lang="urdu"):
    if lang == "urdu":
        print(f"Assalam o Alaikum, {name}!")
    elif lang == "english":
        print(f"Hello, {name}!")
    else:
        print(f"Greetings, {name}!")


name = input("Enter your name: ")
lang = input("Enter language (urdu/english): ")

greet(name, lang)