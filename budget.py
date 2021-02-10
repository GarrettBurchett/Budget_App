class Category:
    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amt, description=""):
        self.amt = -1 * amt
        self.description = description

    def get_balance(self, category):
        self.category = category

    def transfer(self, trans_amt, category):
        self.trans_amt = trans_amt
        self.category = category

    def check_funds(self, amount):
        self.amount = amount





def create_spend_chart(categories):
    pass