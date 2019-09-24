
class Customer():
    balance = 0
    name = "default"

    # Constructor
    def __init__(self, name="default", balance=0):
        self.name = name
        self.balance = balance

    def add_balance(self, amount):
        self.balance += amount

    




guy = Customer()
guy.name = "guy"
guy.add_balance(7)

jacob = Customer()
jacob.name = "jacob"

print(jacob.name)
print(jacob.balance)
print(guy.name)

print(guy.balance)
print(jacob.balance)

bob = Customer(name="bob",balance=20)
print(bob.name)
print(bob.balance)
# bob.other = 7
# print(bob.other)


