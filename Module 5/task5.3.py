# Inheritance: an Animal parent class, with Dog and Cat child classes that print their sound. 

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks: Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows: Meow! Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.make_sound() 
cat.make_sound()  