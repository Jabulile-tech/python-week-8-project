class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount

    def remaining(self):
        return self.limit - self.spent
