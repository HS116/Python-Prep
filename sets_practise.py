#Remem sets are mutable and remove all duplicates. 
#Implemented like a dictionary behind the scenes. 
# O(1) to find an element in a set

vowels = {"a", "e", "i", "o", "u"}
new_set = set()
squares = {x*x for x in range(10)}
print("e" in vowels)

letters = set("alice")
#Intersection, union,add operations using sets
print(letters.intersection(vowels))
print(letters.union(vowels))
letters.add('b')
print(letters)

#Frozen sets: basically just immutable sets
#Because they are immutable, they can be hashable, hence used as keys in dictionaries etc
vowels = frozenset({"a", "e", "i", "o", "u"})

#The below code would throw an error since frozenset is immutable, i.e. can not add to it
#vowels.add("p")


#Multisets: Basically these are sets that allow us to have duplicates
#Hence multisets are often used to not only keep track of whether an element is in the set
#But also how many occurences of the element there are in the set

#Multisets in Python are implemented using the Counter class

from collections import Counter
inventory = Counter()

loot = {"sword" : 1, "bread" : 3}
inventory.update(loot)
print(inventory)

more_loot = {"sword" : 1, "apple": 1}
inventory.update(more_loot)
print(inventory)

# "len" btw returns the number of unique elements
print(f"Number of unique elements: {len(inventory)}")

#Whereas "sum" in combination with ".values()" return the total number of elements
print(f"Total number of elements: {sum(inventory.values())}")
