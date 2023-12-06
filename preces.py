class product:
    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type
    
    def add(self, amount):
        self.amount = self.amount + amount

    def val(self):
        return [self.name, self.amount, self.type]
        
