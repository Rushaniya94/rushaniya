import sqlite3

conn= sqlite3.connect('example.db')

testCursor= conn.cursor()

first=('''
CREATE TABLE IF NOT EXISTS orders(
    order_id   INT PRIMARY KEY,
    order_name TEXT,
    quantity INTEGER    
)
''')

second=('''
CREATE TABLE IF NOT EXISTS employees (
    employees_id   INT PRIMARY KEY,
    name TEXT,
    last_name TEXT,
    salary INTEGER    
)      
       
''')

third=('''
CREATE TABLE IF NOT EXISTS product(
    product_id   INT PRIMARY KEY,
    product_name TEXT,
    category INTEGER    
)       
       
''')

insert_first=('''
INSERT OR IGNORE orders( order_id, product_name, quantity)
VALUES
(12345, 'laptop', 20), 
(67890, 'computer', 10),
(10202,'phone', 30);          
              
              ''')

insert_second=('''
INSERT OR IGNORE employees( employeeID, name, last_name, salary)
VALUES
(1, 'A','E', 20), 
(2, 'B','R', 10),
(3,'C','W', 30),
(4,'D','T', 40);                                        
              ''')

insert_third=('''
INSERT OR IGNORE products( product_id, product_name,category)
VALUES
(1, 'Apple','fruit'), 
(2, 'Banana','fruit'),
(3,'Pear','fruit'),
(4,'Grapes', 'fruit');                                        
              ''')

testCursor.execute(first)
testCursor.execute(second)
testCursor.execute(third)
testCursor.execute(insert_first)
testCursor.execute(insert_second)
testCursor.execute(insert_third)

select_first="SELECT * FROM orders"
testCursor.execute(select_first)
rows=testCursor.fetchall()
for row in rows:
    print(row)
