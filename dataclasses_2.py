from dataclasses import dataclass

from collections import namedtuple

from typing import List

@dataclass
class DataClassCard:
    rank : str
    suit : str

queen_of_hearts = DataClassCard("Q", "Hearts")

DataClassCard2 = namedtuple("DataClassCard2", "rank suit")
queen_of_hearts2 = DataClassCard2("Q", "Hearts")

# Dataclasses are mutable

queen_of_hearts.rank = "Queen"

print(queen_of_hearts)

# Whereas named tuples are not
try:
    queen_of_hearts2.rank = "Queen"

except Exception as AttributeError:
    print("Exception: Named tuples are immutable")


@dataclass(order=True)
class Card:
    rank : str 
    suit : str


RANKS = "2 3 4 5 6 7 8 9 J Q K A".split()
SUITS = "Hearts Clubs Diamonds Spades".split()

def make_deck():
    return [(rank, suit) for rank in RANKS for suit in SUITS]

from dataclasses import field

@dataclass
class Deck:
    # Because it is a default parameter it will be created once for all of the classes
    # so if we want it to be unique for the particular dataclass object then we have to use a field and factory method
    cards : List[Card] = field(default_factory=make_deck)


deck1 = Deck()
deck1.cards.append(Card("?", "Wildcard"))
print(deck1)

# Notice how the decks are independent since we used the field + factory method so the default argument does it not apply to the entire class

deck2 = Deck()
print(deck2)