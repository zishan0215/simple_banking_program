## Class definitions for the bank project
import pickle

class Bank:
    ## constructors
    def __init__(self):
        self.name = "The Python Bank"
        self.addr = "Zishan's Laptop"
        try:
            fp = open('bank.txt')
            bank = pickle.load(fp)
            self.capital = bank['capital']
            self.customers = bank['customers']
            self.employees = bank['employees']
            fp.close()
        except IOError:
            fp = open('bank.txt', 'w')
            bank = {'capital': 50000000, 'employees': 1, 'customers': 0}
            pickle.dump(bank, fp)
            self.capital = bank['capital']
            self.customers = bank['customers']
            self.employees = bank['employees']
            fp.close()

    def __str__(self):
        return self.name + '\n' + self.addr + '\nCapital: $' + str(self.capital) + '\nEmployees: ' + str(self.employees) + '\nCustomers: ' + str(self.customers)

class Employees:
    ## constructors
    def __init__(self):
        try:
            fp = open('employees.txt')
            self.employees = pickle.load(fp)
            fp.close()
        except IOError:
            fp = open('employees.txt', 'w')
            self.employees = {'Joe':10000}
            pickle.dump(self.employees, fp)
            fp.close()

    def __str__(self):
        s = "Name\tSalary\n"
        for name in self.employees.keys():
            s += name + '\t' + str(self.employees[name]) + '\n'
        return s


class Customers:
    ## constructors
    def __init__(self):
        try:
            fp = open('customers.txt')
            self.customers = pickle.load(fp)
            fp.close()
        except IOError:
            fp = open('customers.txt', 'w')
            self.customers = {}
            pickle.dump(self.customers, fp)
            fp.close()

    def __str__(self):
        if self.customers == {}:
            return "No customers\n"
        else:
            s = "Name\t\tAccount Number\t\tBalance\n"
            for acc_number in self.customers.keys():
                s += str(self.customers[acc_number][0]) + '\t\t' + str(acc_number) + '\t\t' + str(self.customers[acc_number][1]) + '\n'
            return s                
    
    ## methods
    def update(self, acc_number):
        fp = open('customers.txt', 'w')
        pickle.dump(self.customers, fp)
        fp.close()
        
    def add_customer(self, name = '', deposit = 1000):
        import random
        x = random.randrange(1000, 10000000)
        acc_number = 100000000 + x
        while acc_number in self.customers:
            x = random.randrange(1000, 10000000)
            acc_number = 100000000 + x
        self.customers[acc_number] = [name, deposit]
        self.update(acc_number)
        return "Customer added"

    def check_balance(self, acc_number):
        if acc_number in self.customers:
            return self.customers[acc_number]
        else:
            return "Not Found"

    def deposit(self, acc_number, amount):
        if amount < 1:
            return "Invalid amount"
        elif acc_number not in self.customers:
            return "Customer not found"
        else:
            self.customers[acc_number][1] += amount
            self.update(acc_number)

    def withdraw(self, acc_number, amount):
        if acc_number in self.customers:
            if amount > 0 and amount <= self.customers[acc_number][1]:
                self.customers[acc_number][1] -= amount
                self.update(acc_number)
            else:
                return 'Invalid amount'
        else:
            return 'Customer not found'
        
cus = Customers()
print cus





