                    # Database Connectivity

# Create a file:
import sqlite3 

# it is used to connect to the database,if it does not exist it will create a new one
conn = sqlite3.connect('iiitdwd')



# Creating tables:
import sqlite3

conn = sqlite3.connect('iiitdwd.db')
# cursor is used to execute SQL commands
cur = conn.cursor()


# for executing multiple query we have take triple code
cur.execute('create table Students(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references Dept(deptno))')


conn.commit()   # commit is important for DML queries
cur.close()
conn.close() 


#inserting value in table:
import sqlite3

conn = sqlite3.connect('iiitdwd.db')
cur = conn.cursor()
cur.execute('insert into Dept(name,deptno) values("Civil",50)')
cur.execute('insert into Dept values(10,"CSE")')
cur.execute('insert into Dept values(20,"DSAI")')
cur.execute('insert into Dept values(30,"ECE")')
cur.execute('insert into Dept values(40,Mech)')


conn.commit()   # commit is important for DML queries
cur.close()
conn.close() 



# SECOND METHOD:
import sqlite3

conn = sqlite3.connect('iiitdwd.db')
cur = conn.cursor()
dno = int(input("Enter deptno:"))
dname = input("Enter dname:")


cur.execute(f'insert into Dept values({dno},"{dname}")')
conn.commit()   # commit is important for DML queries
cur.close()
conn.close() 



# # THIRD METHOD:
import sqlite3

conn = sqlite3.connect('iiitdwd.db')
cur = conn.cursor()
for i in range(1,15):
    
    name =  input("Enter name of students:")
    city =  input("Enter name of city:")
    dno = int(input("Enter deptno:"))
    cur.execute(f'insert into Students values({i} ,"{name}","{city}",{dno})')   

conn.commit()   # commit is important for DML queries
cur.close()
conn.close() 



#FETCHONE() OR FETCHMANY()
import sqlite3

conn = sqlite3.connect('iiitdwd.db')
cur = conn.cursor()
rows = cur.execute('select * from Dept') 
print(rows.fetchone())
print(rows.fetchmany(3))
print(rows.fetchall())

cur.close()
conn.close() 



#Querises:
import sqlite3

conn = sqlite3.connect('iiitdwd.db')
cur = conn.cursor()
rows = cur.execute('select name from Students')  #( It contains Queries):  # We have to use triple code to write Queries in multiple line
allrows = (rows.fetchall())

for t in allrows:
    print(t[0])

cur.close()
conn.close() 



# Update and Delete:
import sqlite3

conn = sqlite3.connect('iiitdwd.db')
cur = conn.cursor()
for i in range(2,8):
    rows = cur.execute(f"delete from Students where roll = {i}")  
    rows = cur.execute("update set name='Robotics' where name = 'Aero' ")  


conn.commit()

cur.close()
conn.close() 