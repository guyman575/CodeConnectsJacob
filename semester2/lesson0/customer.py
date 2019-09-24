

class Customer():
    ''' include class methods and variables here '''
    num_customers = 0

    def __init__(self,name,balance=0):
        Customer.num_customers += 1
        self.balance = balance
        self.name = name

    @classmethod
    def rich(cls,name):
        return cls(name, 100000000)
    # balance
    # getBalance()
    def getBalance(self):
        return self.balance
    # deposit()
    def deposit(self,value):
        self.balance += value # shortcut 

    # withdraw()
    def withdraw(self, value):
        self.balance -= value

def main():
    guy = Customer("Guy")
    print(guy.getBalance())
    guy.deposit(100)
    guy.withdraw(1)
    guy.withdraw(1)
    guy.withdraw(1)
    print(guy.getBalance())

    mark_cuban = Customer.rich("Mark Cuban")
    print(f"{mark_cuban.name} has {mark_cuban.balance} dollars!")

    
    print(Customer.num_customers)
    guy.num_customers = 1000
    print(Customer.num_customers)



if __name__ == "__main__":
    main()
