class Pizza:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return f"Pizza: {self.ingredients}"

    @classmethod
    def salami(cls):
        return cls(["cheese", "salami", "tomato", "dough"])
    
    @classmethod
    def margherita(cls):
        return cls(["margherita", "cheese", "dough", "basil"])
    
    @staticmethod
    def area(radius):
        return radius*radius
    

pizza1 = Pizza(["cheese", "pepperoni", "dough"])
print(pizza1)
margherita = Pizza.margherita()
print(margherita)
salami = Pizza.salami()
print(salami)
print(Pizza.area(5.3))