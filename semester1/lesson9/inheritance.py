# Employee
# 1. name
# 2. salary
# 3. receive_paycheck()
# 4. log_hours()

# Customer
# 1. name
# 2. cart
# 3. add_to_cart()
# 4. checkout()


# Manager
# 1. name
# 2. salary
# 3. employees
# 4. receive_paycheck()
# 5. log_hours()
# 6. open_store()
# 7. hold_meetings()

# class SubClass(SuperClass):

class Person:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(self.name)

class Customer(Person):
    def __init__(self,name,cart):
        super().__init__(name)
        self.cart = cart
    
    def add_to_cart(self,item):
        self.cart.append(item)

    def checkout(self):
        self.cart.clear()



class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def receive_paycheck(self):
        pass

    def log_hours(self):
        pass

    def print_name(self):
        print("Employee " + self.name)

class Manager(Employee):
    def __init__(self,name,salary,employees):
        super().__init__(name,salary)
        self.employees = employees

    def open_store(self):
        # we can use self.name even though it’s not in the Manager __init__()
        # method because Manager INHERITED it from Employee !
        print(self.name + " opened the store")

    def hold_meeting(self):
        pass

    def print_name(self):
        super().print_name()
        print("Manager " + self.name)

emp1 = Employee("bob","30000")
manager1 = Manager("frank","60000",[emp1])

manager1.print_name()
emp1.print_name()

    #         Person
    # Customer---------Employee
    #                     -------Manager

# The method that exists in the lowest level class in the tree that the object has access to
# is what will get called