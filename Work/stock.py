from typedproperty import *
class Stock():
    
    #__slots__ = ['name', '_shares', 'price']
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property    
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares = self.shares - shares
        if not self.shares:
            self.shares = 0

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
