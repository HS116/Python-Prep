import collections

d = collections.OrderedDict(one=1, two=2, three=3)

print(d)
d["four"] = 4

print(d.keys())

#VERY USEFUL
#Default dict: aka we return default values for missing keys
#Default dicts are quite nice cuz we don't have to write extra lines of code 
# to handle KeyError Exceptions anymore
from collections import defaultdict
#So here the default value is an empty list
dd = defaultdict(list)

#E.g. here we are trying to access a missing key "dog", 
# and it will automatically initialize it with the empty list
#so now it is possible for us to immediately append to it. 

dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

print(dd["dogs"])

#Here the default value is a float, which in this case means a 0.0
grades = defaultdict(float)
grades["Neil"] = 2.0
grades["Kai"] = 1.0
print(grades["Konst"])

#Here default value is int, which means 0
siblings = defaultdict(int)
print(siblings["Neil"])

#Chain Map allows us to search through multiple dictionaries at the same time

from collections import ChainMap
dict1 = {"one": 1, "two": 2}
dict2 = {"three" : 3, "four": 4}

chain = ChainMap(dict1, dict2)

print(chain["three"])
print(chain["one"])

#Mapping Proxy Type
#Allow us to create a wrapper around a dictionary to make it read only
#Hence we don't need to make a copy of the dictionary, but rather just add a wrapper

from types import MappingProxyType
writable = {"one" : 1, "two" : 2}
read_only = MappingProxyType(writable)

print(read_only["one"])

#But the following line of code would throw an exception
#read_only["two"] = 4
