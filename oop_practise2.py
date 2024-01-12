class Dog:

    # class attribute
    species = "dog"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def speak(self, sound):
        print(f"{self.name} says {sound}")

dog1 = Dog("Joe", 3)
dog1.speak("hi")
print(Dog.species)
print(dog1.species)

# Inheritance
class GoldenRetriever(Dog):

    # override the method
    def speak(self, sound="woof"):
        super().speak(sound)


goldenRetrierver = GoldenRetriever("jack", 4)
goldenRetrierver.speak()