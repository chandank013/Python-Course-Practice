# Company employees data
import sqlite3

# it is used to connect to the database,if it does not exist it will create a new one
conn = sqlite3.connect('company.db')   # ' ' in single code we can also give the path
# cursor is used to execute SQL commands
cur = conn.cursor()  


# for executing multiple query we have take triple code (int=Integer replaceable)
cur.execute('''
create Table If Not Exists employee(
    id Integer Primary Key,
    name Text Not Null,
    age Integer, 
    department Text
    )  
''')   

# Insert the data in database
cur.execute('''
Insert Into employee(name,age,department)
            values
            ('Chandan',20,'Data Scientist'),
            ('Nitish',21,'Data Analyst'),
            ('Prem',19,'AI Engineer'),
            ('Ravi',21,'ML Expert'),
            ('Suraj',22,'Java Developer')
''')      

conn.commit()  # it may sure that it really affect the database

# Retrieve the data from database
cur.execute('Select * from employee')
rows = cur.fetchall()

# Print the quiryed data
for t in rows:
    print(t)

# cur.close()
# conn.close()