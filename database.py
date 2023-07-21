import sqlite3
con  = sqlite3.connect('univ.db')
cur = con.cursor()

# dno = int(input('Enter Deptno: '))

# dname = input('Department Name: ')

# cur.execute(f'insert into Dept values ({dno}, "{dname}")')

# con.commit()
rows = cur.execute('select * from Dept')
print(rows.fetchall())

cur.close()
con.close() 
