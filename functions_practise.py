def f1(qty, item, price):
    print (f"{qty} {item} cost ${price:.2f}")


#Positional arguments: The order does matter

f1(5, 'bananas', 9.88)

#Keyword arguments: The order does not matter

f1(price=9.88, qty="5", item='bananas')


#But when calling for both positional arguments and keywords arguments, no argument can be left out

#If u wanna leave out an argument, then u must define the function using default/optional parameters


def f2(price, qty=1, item='bananas'):
    print (f"{qty} {item} cost ${price:.2f}")

f2(9.88)
f2(10.9, qty=5)

#But REMEM a non-default parameter can NOT follow a default parameter
#I.e. all the non-default parameters must be stated first, and then u can declare the default parameters. 


#Also BE CAREFUL with default mutable parameters as seen below!!!


def f3(my_list=[]):
    my_list.append("###")
    return my_list

print(f3())
print(f3())
print(f3())
print(f3())

#Notice how above the list is in fact growing,
# this is because default parameter values are only defined once
# Hence each time u call f3() without a parameter you are appending to the same list

#Solution is to perhaps a to create a default argument value that signals no argument has been specified
#e.g. None

def f4(my_list = None):
    if not my_list:
        my_list = []

    my_list.append("###")
    return my_list

print(f4())
print(f4())
print(f4())
print(f4())

'''How does argument passing work in Python exactly?
It's not as clear cut as saying it is call by value or call by reference. 

First of all in Python every piece of data is an object. 
And a reference points to an object, NOT a specific memory location. 

E.g. below first statement causes x to point initially to an object with value of 5
Then the second statement reassigns x to a different object with value of 10. 

We are not overriding the values stored at the memory addresses!!!
'''


def f(fx):
    fx=10

x=5
f(x)
print(x)

#x is still 5, since initially in the function f() fx points to the same object as x does
# But then when we try to set it to 10, it will then rebind/point to a different object which has the value 10
# Hence x is unchanged 

#Thus Python is often called by Object or called by Assignment
# It is neither call by reference nor call by value. 

#But if we pass in a list or any mutable object, then although we still cannot change the whole object wholesale
#since we would rebinding the variable within the function to a different object
#But we could still change the individual elements/members of the mutable object e.g. list

#Example of a modifying a mutable object (dictionary) passed into a function
def f(x):
    x['bar'] = 22

my_dict = {'foo' : 1, 'bar' : 2, 'baz' : 3}

f(my_dict)
print(my_dict)


'''
Summary - Passing an immutable object is kinda like call by value since u don't change the object. 

Passing a mutable object is somewhat like call by reference. You cannot change the object wholesale, but u can still modify elements within the object. 

'''


#Argument Tuple Packing
#This allows us to enter a nice way to enter a variable number of arguments

#If an argument is preceded by an asterisk (*) then this is argument tuple packing
#which means the corresponding arguments (e.g. 1,2,3 in our example below) are packed into a tuple

def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)

f(1,2,3)

def f(x):
    x = 5

x = 10
f(x)
print(x)


