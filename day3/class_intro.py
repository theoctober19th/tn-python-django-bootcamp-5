class Account():
    def withdraw(self, amt):
        self.balance -= amt

    def deposit(self, amt):
        self.balance += amt

    def show_balance(self):
        print("Balance of", self.name, 'is', self.balance) 

    def transfer_balance(self, receiver, amount):
        self.withdraw(amount)
        receiver.deposit(amount)

    def __init__(self, name, initial_amount=0):
        self.name = name
        self.balance = initial_amount

    def __str__(self):
        return self.name



acc1 = Account('Bikalpa')
acc2 = Account('Apple', 1000)

acc2.transfer_balance(acc1, 500)
acc2.show_balance()
print(acc1)