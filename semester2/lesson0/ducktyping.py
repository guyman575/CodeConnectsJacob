
class Dog:
    def bark(self):
        print("WOOF")

class Duck:
    def quack(self):
        print("QUACK")


def main():
    animal = Dog()
    animal.bark()
    print(type(animal) is Dog)
    animal = Duck()
    animal.quack()

if __name__ == "__main__":
    main()