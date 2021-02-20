class Category:
    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.ledger = []
        #title = cat_name.center(30, '*')
        #formatted_ledger = []
        #for k, v in self.ledger.items():
            #formatted_ledger.append(f"{k[:24]} {v.rjust(7)}\n")
        
        #return f"{title}\n{formatted_ledger}\n'Total:' {self.cat_name.get_balance()}"

    def deposit(self, deposit_amt, deposit_desc=""):
        self.deposit_amt = deposit_amt
        self.deposit_desc = deposit_desc
        self.ledger.append({'amount': deposit_amt, 'description': deposit_desc})

    def withdraw(self, withdraw_amt, withdraw_desc=""):
        self.withdraw_amt = withdraw_amt
        self.withdraw_desc = withdraw_desc
        if self.check_funds(withdraw_amt):
            self.ledger.append({'amount': -1 * withdraw_amt, 'description': withdraw_desc})
        else:
            return False

    def get_balance(self):
        self.balance = 0
        for item in self.ledger:
            for value in item.values():
                try:
                    self.balance + float(value)
                except ValueError:
                    pass
            
        return self.balance

    def transfer(self, trans_amt, category):
        self.trans_amt = trans_amt
        self.category = category
        if self.category.check_funds(trans_amt):
            self.category.withdraw(trans_amt, f"Transfer to {self.cat_name}")
            self.deposit(trans_amt, f"Transfer from {category}")
        else:
            return False

    def check_funds(self, amount):
        self.amount = amount
        return amount <= self.get_balance()

def create_spend_chart(categories):
    pass