class Transaction:
    def __init__(self, amount, category, t_type, date, note=""):
        self.amount = amount
        self.category = category
        self.type = t_type  # "income" or "expense"
        self.date = date
        self.note = note

    def to_dict(self):
        return self.__dict__
