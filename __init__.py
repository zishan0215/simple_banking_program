import sqlite3

if __name__ == '__main__':
    con = sqlite3.connect('bank_data.db')
    con.execute('''
                    CREATE TABLE bank (id INT(11) PRIMARY KEY,
                    name VARCHAR(40) NOT NULL, location VARCHAR(40) NOT NULL, capital
                    DOUBLE NOT NULL, customers INT(11), employees INT(11));
                ''')
    con.execute('''
                    CREATE TABLE customers(id INT(11) PRIMARY KEY NOT NULL,
                    name VARCHAR(40) NOT NULL, password VARCHAR(40), balance DOUBLE, 
                    loans INT(11), account_number INT(11) NOT NULL, credit_card_number INT(11));
                ''')
    con.execute('''
                    CREATE TABLE employees(id INT(11) PRIMARY KEY NOT NULL, 
                    name VARCHAR(40), password VARCHAR(40), salary DOUBLE, 
                    position VARCHAR(40), location VARCHAR(40));
                ''')
    con.commit()

    con.execute('''
                    INSERT INTO bank(id, name, location, capital, customers, employees)
                    VALUES (1,'The Python Bank', 'Toshiba Satellite', 10000000,
                    0, 1);
                ''')
    con.execute('''
                    INSERT INTO employees(id, name, password, salary,
                    position, location) VALUES (1, 'Zishan',
                    'Zishan2', 100000, 'CEO', 'Toshiba Satellite');
                ''')
    con.commit()
    con.close()
