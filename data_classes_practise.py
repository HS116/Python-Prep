from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank : str
    suit : str

'''
Dataclass helps make our code more concise
Since it already contains built-in functionality e.g. instantiation, printing, and comparison
'''
#Built in .__init__ method already for construction
queen_of_hearts = DataClassCard('Q', 'Hearts')
#Built in printing (aka .__repr__() functionality)
print(queen_of_hearts)

#Built in .__eq__() functionality aka to compare objects
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))


#Hence dataclasses are for more concise than regular classes, less boiler plate

#Dataclasses are better then regular tuples, since u don't have to remem the order of the attributes
#Named tuples are a better alternative then regular tuples
#However dataclasses are still better than named tuples, 
#Since named tuples do not take into account types when doing comparisons

#E.g.
from collections import namedtuple
NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
Person = namedtuple('Person', ['first_initial', 'last_name'])
ace_of_spades = NamedTupleCard('A', 'Spades')
#This would return true, since the tuples themselves are identical
#However we are not taking account that they have different named tuple types. 
print(ace_of_spades == Person('A', 'Spades'))

#Also another negative of named tuples, is that they are immutable
#But this can also be a positive in other cases

#Data Classes
from typing import Any
@dataclass
class Position:
    #Must specify type annotations when creating a data class
    #But these type annotations are not enforced unless u run a type checker
    name: str
    #Can also have default values
    lon: float = 0.0
    lat: float = 0.0

    #But if u dont' want to speciy a particular type u use "typing.Any"
    value: Any = 42


    #You can also add methods to a dataclass
    def inc_lon(self, value):
        self.lon += value


from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank : str
    suit : str


@dataclass
class Deck:
    cards : List[PlayingCard]

queen_of_hearts = PlayingCard('Q', "Hearts")
ace_of_spades = PlayingCard("A", "Spades")
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)

#Advanced Default Values
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


#For data classes one can only immutable values for default parameters
#This is because if we used a mutable value, and this value then changed, 
# then it would change that particular default parameter for all instances of the class

#To be able to pass in "mutable"like values for default parameters, we have to use field(default_factory=...)
from dataclasses import field
@dataclass
class Deck:
    #Btw field() helps us customize each field of the dataclass
    cards : List[PlayingCard] = field(default_factory = make_french_deck)

french_deck = Deck()
print(french_deck)

#You can also add metadata using field()
@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit' : 'degrees'})
    lat : float = field(default=0.0, metadata={'unit' : 'degrees'})

#MEtadata can then be retreived using fields()
from dataclasses import fields
lat_unit = fields(Position)[2].metadata['unit']
print(lat_unit)

#We can also allow data class objects to be ordered/ranked using "order=True"
#  and then to specify how things are ordered u need to create a field sort_index and then method __post_init__()
#Also we can make the data classes immutable using "frozen=True"
#E.g.
@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat : float = 0.0

#But remem though just because the dataclass object itself is immutable
#doesn't mean that the fields within the object must also be immutable, they could be mutable

#This holds true for all nested data structures. 

#In addition we can also have inheritance with dataclasses

@dataclass 
class Position_No_Default:
    name: str
    lon: float
    lat : float


@dataclass
class Capital(Position_No_Default):
    country:str

#But it's more complicated if the parent class has default arguments. 

#cuz REMEM a non-default argument can NOT follow a default argument in Python
#I.e. if a paramter has a default value, then all following parameters must have default values
#Hence if there is a field in the parent class which has a default value,
#  then all the inherting classes must contain only default paramters. 


