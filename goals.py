class Goal:
    def __init__(self, name, target_amount):
        self.name = name
        self.target_amount = target_amount
        self.saved_amount = 0

    def add_savings(self, amount):
        self.saved_amount += amount

    def is_complete(self):
        return self.saved_amount >= self.target_amount
