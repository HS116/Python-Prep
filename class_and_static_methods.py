class MyClass:
    
    def method(self):
        #This method can modify both the object state (through self) as well as the class state
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        #This method can modify only the class state
        return "class method called", cls

    @staticmethod
    def staticmethod():
        #This method can NOT modify the object state nor the class state. 
        #Basically these are just functions that are apart of the class's namespace
        return "static method called"

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())
#But the below code would throw an error since we need an instance of the class
#print(MyClass.method())


import math
class Pizza:
    def __init__(self, ingredients, radius=5):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f"Pizza({self.ingredients}, {self.radius}cm)"


    #Very helpful use case of class methods is to have alternative constructors
    #E.g.

    @classmethod
    def margherita(cls):
        #Notice how we're using "cls" instead of "Pizza"
        #This is good cuz we don't repeat ourselves and if we change the name of the class "Pizza" to something else, 
        # we don't have to change these class methods at all. 
        return cls(["mozarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozarella", "tomatoes", "ham"])

    #Btw remem in Python u can only have one .__init__ method
    #Hence class methods are a useful way of creating alternative constructors. 

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


pizza1 = Pizza(["cheese", "tomatoes"], 12)
print(pizza1)

print(Pizza.margherita())
print(Pizza.prosciutto())
print(pizza1.area())
