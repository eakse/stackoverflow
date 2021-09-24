class Category:
    def __init__(self):
        self.ledger = []
        # total also needs the "self." to make it an instance variable, just
        # as the ledger above
        # if you omit the "self."" it's a localized variable only available
        # to the __init__ method itself.
        self.total = 0

    def deposit(self, amount, *description):
        self.ledger.append({"amount": amount, "description": description})
        # add the amount to the total
        self.total += amount
        return self.ledger

    def withdraw(self, withdrawal):
        # make the withdrawal negative
        if abs(withdrawal) == withdrawal:
            withdrawal = 0 - withdrawal
        # check if there's enough in the total
        if abs(withdrawal) <= self.total:
            # update the total
            self.total += withdrawal
            # add to the ledger
            self.ledger.append({"withdrawal": withdrawal})
        else:
            # you could return an error message here
            pass
        return self.ledger

    def update_total(self):
        total = 0
        for item in self.ledger:
            # need to check if the amount key is in the dict object
            if "amount" in item:
                total += item["amount"]
            # this check below is not needed but it ensures future compatability
            elif "withdrawal" in item:
                total += item["withdrawal"]
        # just because, you can check if the totals match
        if self.total != total:
            print(
                f"""Difference in totals found. Someone is cheating :-|
  Instance total:   {self.total}
  Calculated total: {total}"""
            )
        # set the instance variable to the local variable
        self.total = total
        return self.total



from pprint import pprint
nr1 = Category()
nr2 = Category()

for i in range(10):
    nr1.deposit(i, f"deposit - {i}")

pprint(nr1.ledger)
print(f"Total: {nr1.total}")
nr1.withdraw(10)
print(f"Total: {nr1.total}")
nr1.withdraw(-10)
print(f"Total: {nr1.total}")
nr1.withdraw(99999)
print(f"Total: {nr1.total}")
pprint(nr1.ledger)
print(nr1.update_total())
nr1.total = 123
print(nr1.update_total())

# just to show that the above only updated the values inside the nr1 instance.
print(f"Total for nr2: {nr2.total}")