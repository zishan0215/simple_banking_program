## Class definitions for the bank project
import pickle
import os
import random
import sqlite3


class Bank:
    attr = {'id': 0, 'name': 1, 'location': 2, 'capital': 3,
            'customers': 4, 'employees': 5}
    ## constructors

    def __init__(self):
        con = sqlite3.connect('bank_data.db')
        cur = con.execute('SELECT * FROM bank WHERE id = 1;')
        for i in cur:
            self.name = i[self.attr['name']]
            self.addr = i[self.attr['location']]
            self.capital = i[self.attr['capital']]
            self.customers = i[self.attr['customers']]
            self.employees = i[self.attr['employees']]
        con.close()

    def __str__(self):
        return self.name + '\n' + self.addr + '\nCapital: $' + str(self.capital) + '\nEmployees: ' + str(self.employees) + '\nCustomers: ' + str(self.customers)


class Employees:
    ## Properties
    attr = {'id': 0, 'name': 1, 'password': 2, 'salary': 3, 'position': 4,
            'location': 5}
    employees = {}

    ## constructors
    def __init__(self):
        con = sqlite3.connect('bank_data.db')
        cur = con.execute('SELECT * FROM employees')
        for i in cur:
            self.employees[i[self.attr['id']]] = [i[self.attr['id']],
                                                  i[self.attr['name']],
                                                  i[self.attr['password']],
                                                  i[self.attr['salary']],
                                                  i[self.attr['position']],
                                                  i[self.attr['location']]]
        con.close()

    def __str__(self):
        s = "Id\tName\t\tSalary\t\tPosition\tLocation\n"
        for eid in self.employees.keys():
            s += str(eid) + '\t' + self.employees[
                eid][self.attr['name']] + '\t\t'
            s += str(self.employees[eid][self.attr['salary']]) + '\t'
            s += self.employees[eid][self.attr['position']] + '\t\t'
            s += self.employees[eid][self.attr['location']] + '\n'
        return s

    ## methods
    def get_id(self, ename):
        for i in self.employees.keys():
            if self.employees[i][self.attr['name']] == ename:
                return i
        return -1

    def check_login(self, ename, epassword):
        eid = self.get_id(ename)
        if eid == -1:
            return -1
        if self.employees[eid][self.attr['name']] == ename:
            if self.employees[eid][self.attr['password']] == epassword:
                return 1
            else:
                return -2
        else:
            return -3


class Customers:
    attr = {'id': 0, 'name': 1, 'password': 2, 'balance': 3, 'loans': 4,
            'account_number': 5, 'credit_card_number': 6}
    customers = {}
    ## constructors

    def __init__(self):
        con = sqlite3.connect('bank_data.db')
        cur = con.execute('SELECT * FROM customers')
        for i in cur:
            self.customers[i[self.attr['account_number']]] = [i[self.attr['id']],
                                                              i[self.attr['name']],
                                                              i[self.attr['password']],
                                                              i[self.attr['balance']],
                                                              i[self.attr['loans']],
                                                              i[self.attr['account_number']],
                                                              i[self.attr['credit_card_number']]]
        con.close()

    def __str__(self):
        if self.customers == {}:
            return "No customers\n"
        else:
            s = "Id\tName\t\tAccount Number\t\tBalance\t\tCredit Card Number\n"
            for acc_num in self.customers.keys():
                s += str(self.customers[acc_num][self.attr['id']]) + '\t'
                s += self.customers[acc_num][self.attr['name']] + '\t\t'
                s += str(self.customers[acc_num][self.attr['account_number']]) + '\t\t'
                s += str(self.customers[acc_num][self.attr['balance']]) + '\t\t'
                s += str(self.customers[acc_num][self.attr['credit_card_number']]) + '\n'
            return s

    ## methods
    def update(self):
        self.__init__()

    def update_loan(self, acc_number, loan_detail):
        path = 'loan/' + str(acc_number) + '.txt'
        fp = open(path, 'a')
        pickle.dump(loan_detail, fp)
        fp.close()

    def create_loan(self, acc_number, loan_detail):
        path = 'loan/' + str(acc_number) + '.txt'
        fp = open(path, 'w')
        pickle.dump(loan_detail, fp)
        fp.close()

    def add_customer(self, cname='', cpassword='', cdeposit=1000.00):
        x = random.randrange(1000, 10000000)
        acc_number = 100000000 + x
        con = sqlite3.connect('bank_data.db')
        i = 0
        cur = con.execute('SELECT * FROM customers WHERE account_number = %d' % (acc_number))
        for i in cur:
            pass
        while i != 0:
            x = random.randrange(1000, 10000000)
            acc_number = 100000000 + x
            i = 0
            cur = con.execute('SELECT * FROM customers WHERE account_number = %d' % (acc_number))
            for i in cur:
                pass
        query = '''
                        INSERT INTO customers(id, name, password, balance,
                        loans, account_number, credit_card_number) VALUES
                        (%d, '%s', '%s', %f, %d, %d, %d);
                ''' % (1, cname, cpassword, cdeposit, 0, acc_number, 0)
        print query
        try :
            con.execute(query)
            con.commit()
            con.close()
            self.update()
        except Exception as e :
            print e
            return "Error"
        return "Customer added"

    def check_balance(self, acc_number):
        if acc_number in self.customers:
            return self.customers[acc_number]
        else:
            return "Customer not Found"

    def get_amount(self, acc_number):
        x = self.check_balance(acc_number)
        return x[3]

    def deposit(self, acc_number, amount):
        if acc_number in self.customers:
            if amount < 1:
                return "Invalid amount"
            elif acc_number not in self.customers:
                return "Customer not found"
            else:
                amount += self.get_amount(acc_number)
                con = sqlite3.connect('bank_data.db')
                con.execute('''UPDATE customers SET balance = %d
                            WHERE account_number = %d''' % (amount, acc_number))
                con.commit()
                con.close()
                self.update()
                return 'Amount deposited. \nTotal balance: %d' % (amount)
        else:
            return 'Customer not found'

    def withdraw(self, acc_number, amount):
        if acc_number in self.customers:
            if amount > 0 and amount <= self.customers[acc_number][self.balance]:
                self.customers[acc_number][self.balance] -= amount
                self.update(acc_number)
            else:
                return 'Invalid amount'
        else:
            return 'Customer not found'

    def loan(self, loan_amount, period, salary, acc_number):
        credit = loan_amount + (loan_amount * 0.1 * period)
        emi = credit / period
        print emi
        if acc_number in self.customers:
            if emi > (salary * 0.45):
                return 'Loan cannnot be sanctioned'
            else:
                self.customers[acc_number][self.balance] += loan_amount
                self.update(acc_number)
                x = random.randrange(1000, 50000000)
                loan_id = 500000000 + x
                self.loan_detail.append(
                    [loan_id, loan_amount, emi, credit, period])
                file_name = str(acc_number) + '.txt'
                if file_name in os.listdir('loan/'):
                    self.update_loan(acc_number, self.loan_detail)
                else:
                    self.create_loan(acc_number, self.loan_detail)
                return 'Loan sanctioned'
        else:
            return 'Customer not found'

    def print_loan_details(self, acc_number):
        path = 'loan/' + str(acc_number) + '.txt'
        fp = open(path)
        x = pickle.load(fp)
        print 'Loan Id\t\tLoan Amount\tEMI\t\tTotal Amount\tPeriod'
        for i in range(len(x)):
            print x[i][self.loan_id], '\t', x[i][self.loan_amount], '\t\t', x[i][self.emi], '\t\t', x[i][self.credit], '\t\t', x[i][self.period]

    def pay_emi(self):
        pass

    def check_login(self, acc_number, cpassword):
        if acc_number in self.customers.keys():
            if self.customers[acc_number][self.attr['password']] == cpassword:
                return 1
            else:
                return -1
        else:
            return -2


if __name__ == '__main__':
##    cid = 109314064
##    cus = Customers()
## print cus
## print cus.check_balance(cid)
##    cus.deposit(cid, 2000)
##    cus.withdraw(cid, 190000)
## print cus.check_balance(cid)
## print cus.loan(1000, 10, 40000, cid)
## print cus.check_balance(cid)
## cus.print_loan_details(cid)
##
##    b = Bank()
##    print b
##
##    
##    e = Employees()
##    print e
##
    c = Customers()
    print c

##    print c.add_customer('John', 'John2', 1000)
##
##    print c
