squares = [i*i for i in range(10)]
print(squares)

cubes = [i**3 for i in range(15)]
print(cubes)

def inc_1(num):
    return num+1

#"Functional Programming: map, this is an alternative to a list comprehension or for loop"
cubes_plus_1 = list(map(inc_1, cubes))
print(cubes_plus_1)

#Conditional at the end aka to decide whether to be in the list at all i.e. filtering
sentence = "the rocket came back from mars"
vowels = [char for char in sentence if char in "aeiou"]
print(vowels)

#Conditional at the beginning to modify aka decide how to modify the element we will add to our list
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

#Set comprehension, aka no duplicates
quote = "life, uh, finds a way"
vowels = {i for i in quote if i in "aeiou"}
print(vowels)

#Dictionary comprehension
squares = {i : i*i for i in range(10)}
print(squares)
print (squares[5])


#You can also use an "assignment expression" also known as a "walrus operator"
#This allows us to assign an output to a variable and then use this later
#"Assignment Expressions" also make it clearer what the expression means

import random
def get_weather_data():
    return random.randrange(90,110)

hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)

#Generator comprehension
#Generators are particularly useful since they do not load the entire data structure into memory
#But rather return an iterable that yields the next element

#Generator comprehension uses curved brackets
print(sum(i*i for i in range(10000000)))

