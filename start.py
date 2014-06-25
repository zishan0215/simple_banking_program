import classes
e = classes.Employees()
c = classes.Customers()
b = classes.Bank()

def admin_area(name):
    print '\nWelcome %s!' % (name)
    print '\nWhat would you like to do?\n'
    print '1 Check employees'
    print '2 Check customers'
    print '3 Check bank details'
    print '4 Exit\n'
    try:
        choice = input('Enter choice: ')
        print 
        if choice == 1:
            print e
            admin_area(name)
        elif choice == 2:
            print c
            admin_area(name)
        elif choice == 3:
            print b
            admin_area(name)
        else:
            exit()
    except NameError:
            print 'Please Enter a number between 1 and 4'
            admin_area(name)
        

def admin_login():
    print '\n\nWelcome to admin login\n'
    name = raw_input('Enter username: ')
    password = raw_input('Enter password: ')
    check = e.check_login(name, password)
    if check == -1:
        print 'Employee Does Not Exist'
        admin_login()
    elif check == -2:
        print 'Wrong Password'
        admin_login()
    elif check == 1:
        admin_area(name)
    else:
        print "Something's Wrong"

def login():
    pass

def new_customer():
    pass

def interface1():
    print 'Welcome to The Python Bank\n'
    print '1 Customer Login'
    print '2 Admin Login'
    print '3 Exit\n'
    try:
        choice = input('Enter choice: ')
        if choice == 3:
            exit()
        return choice
    except NameError, SyntaxError:
            print 'Please Enter a number between 1 and 3'
            return interface1()

def interface2(choice):
    if choice == 1:
        print '\n\nWelcome to customer login\n'
        print '1 Login'
        print '2 New Customer Account'
        print '3 Exit\n'
        try: 
            choice = input('Enter choice: ')
            if choice == 1:
                login()
            elif choice == 2:
                new_customer()
            elif choice == 3:
                exit()
            else:
                print 'Bad Input'
        except NameError:
            print 'Please Enter a number between 1 and 3'
            interface2(1)
    elif choice == 2:
        admin_login()
    else:
        print 'Bad Input'

if __name__ == '__main__':
    choice = interface1()
    print choice
    interface2(choice)
