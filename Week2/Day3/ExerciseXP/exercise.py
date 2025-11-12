class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __str__(self):
        return f"{self.amount} dollars."
    
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        return f"{self.amount} dollars."
    
    def __add__(self, other):

        if isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise ValueError("Must be same currency")
        elif type(other) == int:
            return self.amount + other
        else:
            raise ValueError("Must be an instance of a currency")
    
    def __iadd__(self, other):
        if isinstance(other, Currency):
            self.amount += other.amount
            return self
        elif type(other) == int:
            self.amount += other
            return self
        else:
            raise ValueError("Must be an instance of a currency")

if __name__=='__main__':
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(c1)
    print(int(c1))
    print(repr(c1))
    print(c1 + 5)
    print(c1 + c2)
    print(c1)
    c1 += 5
    print(c1)
    c1 += c2
    print(c1)
    print(c1 + c3)