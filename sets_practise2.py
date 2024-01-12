# Set
nums = {1, 2, 3, 4, 5}
squares = {i*i for i in range(5)}
evens = {2*i for i in range(10)}
print(nums)
print(squares)


print(nums.intersection(evens))
print(squares.union(evens))

#Frozen sets - i.e. immutable sets
squares_frozen = frozenset(squares)
print(squares_frozen)


# Multisets implemented using counter

from collections import Counter

inventory = Counter()

loot = {"sword":1, "gun": 2}
inventory.update(loot)

loot2 = {"sword": 3, "gun": 1, "rifle": 2}

inventory.update(loot2)

print(inventory)