# # Company employees data
import sqlite3

conn = sqlite3.connect('company.db')

cur = conn.cursor()

# for executing multiple query we have take triple code
# for executing multiple query we have take triple code (int=Integer replaceable)
# cur.execute('''
# create Table If Not Exists employee1(
#     id Integer Primary Key,
#     name Text Not Null,
#     age Integer, 
#     department Text
#     )  
# ''')    

# # Insert the data in database
# cur.execute('''
# Insert Into employee1(name,age,department)
#             values
#             ('Chandan',20,'Data Scientist'),
#             ('Nitish',21,'Data Analyst'),
#             ('Prem',19,'AI Engineer'),
#             ('Ravi',21,'ML Expert'),
#             ('Suraj',22,'Java Developer')
# ''')  


# # Upadate the data in the table
# cur.execute('''
# UPDATE employee1
#         set age=34
#             where name = 'Nitish'
# ''')  


# Delete the data in the table
cur.execute('''
DELETE from employee1
            where name = 'Ravi'
''')  

conn.commit()  # it may sure that it really affect the database

# Retrieve the data from database
cur.execute('Select * from employee1')
rows = cur.fetchall()

# Print the quiryed data
for t in rows:
    print(t)


# cur.close()
# conn.close()