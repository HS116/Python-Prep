#! /usr/bin/python3
# Named tuples
#Similar to tuples in the way that they are immutable
#But they are named haha 
# which means each object in the tuple can be accessed using a modifier rather than an integer index

from collections import namedtuple

p1 = namedtuple("Point", "x y z")(1,2,3)
p2 = (1,2,3)

#Named tuples are implemented as classes in Python, but they consume way less memory

from sys import getsizeof

#Named tuples and regular tuples have the same size
print(getsizeof(p1))
print(getsizeof(p2))

#Named tuples are way easier to read since we have identifiers for each object in the tuple
Car = namedtuple("Car", "color mileage automatic")
car1 = Car("red", 3812.4, True)

#Named tuples also have a cool repr aka they are printed nicely
#Whereas classes have a not so nice default repr, as only the object id will get printed. 
print(car1)

#Practise
Student = namedtuple("Student", "name age grade")
student1 = Student("Neil", 21, 2.2)
print(student1)

Shoe = namedtuple("Shoe", "Brand Size Color")
shoe1 = Shoe("Adidas", 44, "Blue")
print(shoe1)
print(shoe1.Color)
print(shoe1.Size)



#Btw the namedtuple class in the collections module is from Python 2.6+
#We can use typing.NamedTuple which is from Python 3.6+
#which adds support for type annotations

from typing import NamedTuple

class Motorcyle(NamedTuple):
    color : str
    mileage : float
    automatic : bool

motorcycle1 = Motorcyle("red", 133.5, True)
print(motorcycle1)


from collections import namedtuple

Animal = namedtuple("Animal", "name age weight type")
animal1 = Animal("Jeff", 7, 39, "dog")

from typing import NamedTuple

class Animal2(NamedTuple):
    name : str
    age : int
    weight : int
    type : str

animal2 = Animal2("Jeff", 7, 39, "dog")

