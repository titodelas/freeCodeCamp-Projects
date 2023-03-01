class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self._balance = 0.0

    def __repr__(self):
        header = f"{self.description.center(30, '*')}\n"
        ledger = ""
        for item in self.ledger:
            line_description = f"{item['description']:<23}"
            line_amount = f"{item['amount']:>7.2f}"
            ledger += f"{line_description[:23]}{line_amount[:7]}\n"
        total = f"Total: {self._balance:.2f}"
        return f"{header}{ledger}{total}"

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self._balance += amount

    def withdraw(self, amount, description=""):
        if self._balance - amount >= 0:
            self.ledger.append({"amount": -amount, "description": description})
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.description}"):
            category.deposit(amount, f"Transfer from {self.description}")
            return True
        return False

    def check_funds(self, amount):
        return self._balance >= amount


def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_amounts.append(round(abs(spent), 2))

    total = round(sum(spent_amounts), 2)
    spent_percentages = [int(((amount / total) * 10) // 1) * 10 for amount in spent_amounts]

    header = "Percentage spent by category\n"
    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += f"{str(value).rjust(3)}|"
        for percent in spent_percentages:
            chart += " o " if percent >= value else "   "
        chart += " \n"

    footer = "    " + "-" * (3 * len(categories) + 1) + "\n"
    descriptions = [category.description for category in categories]
    max_length = max(map(len, descriptions))
    descriptions = [description.ljust(max_length) for description in descriptions]
    for x in zip(*descriptions):
        footer += "    " + " ".join(s.center(3) for s in x) + " \n"

    return f"{header}{chart}{footer}".rstrip("\n")
