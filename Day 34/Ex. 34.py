class BankAccount:

    interest_rate = 5

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def add_interest(self):
        self.balance += self.balance * (BankAccount.interest_rate/100)

acc1 = BankAccount("Walt", 1500)
acc2 = BankAccount("Jesse", 1400)

acc1.add_interest()
acc2.add_interest()

print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)

BankAccount.interest_rate = 8

acc1.add_interest()
acc2.add_interest()

print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)
