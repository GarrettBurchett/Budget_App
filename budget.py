class Category:
    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.ledger = []
        self.withdrawals = []
    
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
            self.withdrawals.append(withdraw_amt)
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

def calculate_total_spent(categories):
    total_spent = 0
    for category in categories:
        total_spent += sum(category.withdrawals)

    return total_spent

def percentage_spend_per_category(categories, total_spent):
    category_spending = []
    for category in categories:
        category_spend = (sum(category.withdrawals) / total_spent) * 100
        category_spending.append(category_spend)

    return category_spending

def stacked_category_names(categories):
    """Creates the category names to be vertically stacked for the spend chart."""
    formatted_categories = ""
    len_of_longest_name = 0
    for category in categories:
        if len(category.cat_name) > len_of_longest_name:
            len_of_longest_name = len(category.cat_name)
    
    count = 1
    while count <= len_of_longest_name:
        row = []
        for i in range(len_of_longest_name):
            row.append("     ")
            for category in categories:
                if i <= len(category.cat_name)-1:
                    row.append(category.cat_name[i] + "  ")
                else:
                    row.append("   ")
            row_of_letters = "".join(row)
            row.clear()
            if count == len_of_longest_name: # Unit Test failed for having \n on last line. Needed everywhere else.
                formatted_categories += row_of_letters
            else:
                formatted_categories += row_of_letters + "\n"
            count += 1
    
    return formatted_categories

def create_spend_chart(categories):
    dashes = '-' * 10
    y_axis = 100
    chart = "Percentage spent by category\n"

    while y_axis > -1:
        bar = []
        for percent in percentage_spend_per_category(categories, calculate_total_spent(categories)):
            if percent >= y_axis:
                bar.append("o  ")
            else:
                bar.append("   ")
        bars = "".join(bar)
        chart += str(y_axis).rjust(3) + "| " + bars + "\n"
        y_axis -= 10
    
    chart += "    " + dashes + "\n" + stacked_category_names(categories)

    return chart