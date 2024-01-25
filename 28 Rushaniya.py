import sqlite3

conn= sqlite3.connect('example.db')
cursor=conn.cursor()



try:
    conn.execute('BEGIN TRANSACTION')
SAVEPOINT sp1

    
cursor.execute('UPDATE accounts SET balance= balance-100 WHERE user_id=1')
cursor.execute('UPDATE accounts SET balance= balance+100 WHERE user_id=2')
conn.execute('COMMIT')



raise Exception('Simulated error')
except  Exception as e:
conn.execute('ROLLBACK')
print(f'Error:{e}')
conn.close()

ROLLBACK TO SAVEPOINT sp1
COMMIT
