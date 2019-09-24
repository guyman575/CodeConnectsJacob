class Candy():
    # class variable
    taste = "sweet"

    def __init__(self, name):
        # Instance variable
        self.name = name

twix = Candy("Twix")
sourpatch = Candy("Sour Patch")

# sourpatch.taste = "sour"
Candy.taste = "sour"

Candy.name = "test"
print(twix.taste)
print(sourpatch.taste)
print(twix.name)
print(sourpatch.name)


class Dog():
    # Not good
    tricks = ["sit","stay"]

    def __init__(self, name):
        # Instance variable
        self.name = name

fido = Dog("fido")
spot = Dog("spot")
fido.tricks.append("roll over")
# Changed for both dogs
print(spot.tricks)
print(fido.tricks)

# Instance variables are for data unique to each instance and class variables are
# for attributes and methods shared by all instances of the class.