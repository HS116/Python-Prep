class Dog:

    #If the attribute is defined outside the __init__() method, then it will be a class attribute
    species = "Canis familiaris"


    #Remem first parameter of __init__ will always be "self" aka the current instance of the object
    def __init__(self, name, age):
        #name and age are now instance attributes
        self.name = name
        self.age = age

    #Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    #__str__() method helps us with printing an object in a certain way
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


dog1 = Dog("Jeff", 19)
print(dog1.name)
print(dog1.age)
print(dog1.species)
print(Dog.species)
print(dog1.description())
print(dog1)

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

car1 = Car("blue", 20000)
car2 = Car("red", 30000)

print(car1)
print(car2)

class Bulldog(Dog):
    #Overriding the parent class method, so now we have a default argument of "Woof" for sound
    def speak(self, sound="Woof"):
        return super().speak(sound)

jim = Bulldog("Jim", 5)
print(jim.speak("woof"))
print(jim.speak())

print(isinstance(jim, Bulldog))
print(isinstance(jim, Dog))


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


