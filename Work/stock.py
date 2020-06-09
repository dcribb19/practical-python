class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'


    def cost(self):
        cost = self.shares * self.price
        return cost


    def sell(self, n_shares):
        self.shares -= n_shares
        