# pets store has some pets, dogs, cats, birds, etc

class Pet():

    def __init__(self,name):
        self.name = name

    def talk(self):
        print("...")

class Dog(Pet):
    def talk(self):
        print ("Woof")

class GolderRetriever(Dog):
    shed = True

class Poodle(Dog):
    shed = False

class ShiTzu(Dog):
    shed = False
    def talk(self):
        print("Yap")

class Cat(Pet):
    def talk(self):
        print ("Meow") 

class Rabbit(Pet):
    pass

class Fish(Pet):
    pass