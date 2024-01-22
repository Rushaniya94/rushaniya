import sqlite3
conn= sqlite3.connect('mydatabase.db')

cursor=conn.cursor()

create_table_query='''

INSERT INTO  employees (first_name, last_name, job_title)

VALUES ('John', 'Jackson','Software Developer'),
('Bob','Williams','Back-end Developer'),
('Max','Miller','Designer');
'''
select_data_query='SELECT*FROM Employees;'

cursor.execute(select_data_query)
rows=cursor.fetchall()

for row in rows:
    print(row)

employees= session.query(Employee).all()

for person in employees:
    print(f"The employee is {person.id}, the name is {person.name} and the age is {person.age}")

INSERT into employees (salary)
SELECT salary

FROM TemporaryEmployees;

session.commit()