from collections import namedtuple

Student = namedtuple("Student", "name age grade") 

student1 = Student("Neil", 21, 2.0)

print(student1)

from typing import NamedTuple

class NewStudent(NamedTuple):
    name : str
    age : int
    grade : float

student2 = NewStudent("Kai", 21, 1.0)
print(student2)


Player = namedtuple("Player", "name age position")
player1 = Player("Ronaldo", 39, "Striker")

class NewPlayer(NamedTuple):
    name : str
    age : int
    position : str

player2 = NewPlayer("Ronaldo", 39, "Striker")