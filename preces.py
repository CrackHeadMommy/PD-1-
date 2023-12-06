class product:
    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type
    
    def add(self, amount):
        self.amount = int(self.amount) + int(amount)

    def take(self, amount):
        if int(self.amount) < int(amount):
            return False
        self.amount = int(self.amount) - int(amount)
        if self.amount>0:
            return True
        return 

    def val(self):
        return [self.name, self.amount, self.type]
    
    def compare(self):
        return str(self.amount) + " of " + str(self.name) + " which is considered a " + str(self.type)
        
