class Category:
    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.ledger = []
    
    def __str__(self):    
        formatted_ledger = []
        for item in self.ledger:
            for value in item.values():
                if type(value) == str:
                    formatted_ledger.append(f"{item['description'][:23].ljust(23)} {format(item['amount'], '.2f').rjust(6)}\n")
        
        return f"{self.cat_name.center(30, '*')}\n{''.join(formatted_ledger)}Total: {self.get_balance()}"

    def deposit(self, deposit_amt, deposit_desc=""):
        self.deposit_amt = deposit_amt
        self.deposit_desc = deposit_desc
        self.ledger.append({'amount': deposit_amt, 'description': deposit_desc})

    def withdraw(self, withdraw_amt, withdraw_desc=""):
        self.withdraw_amt = withdraw_amt
        self.withdraw_desc = withdraw_desc
        if self.check_funds(withdraw_amt):
            self.ledger.append({'amount': -1 * withdraw_amt, 'description': withdraw_desc})
            return True
        else:
            return False

    def get_balance(self):
        self.balance = 0
        for item in self.ledger:
            for value in item.values():
                try:
                    self.balance += float(value)
                except ValueError:
                    pass
            
        return self.balance

    def transfer(self, trans_amt, cat):
        self.trans_amt = trans_amt
        self.cat = cat
        if self.check_funds(trans_amt):
            self.withdraw(trans_amt, f"Transfer to {cat.cat_name}")
            self.cat.deposit(trans_amt, f"Transfer from {self.cat_name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        self.amount = amount
        return amount <= self.get_balance()

def create_spend_chart(categories):
    pass