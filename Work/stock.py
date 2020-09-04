
class Stock():
    __slots__ = ['name', '_shares', 'price']
    def __init__(self, name, share, price):
        self.name = name
        self.shares = share
        self.price = price

    @property    
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, shares):
        if not isinstance(shares, int):
            raise TypeError('Un expected value, int required')
        self._shares = shares

    @property    
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares = self.shares - shares
        if not self.shares:
            self.shares = 0

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
