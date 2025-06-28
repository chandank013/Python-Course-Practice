# # Company employees data
import sqlite3

conn = sqlite3.connect('sales_data.db')

cur = conn.cursor()


# cur.execute('''
# CREATE TABLE IF NOT EXISTS sales(
#     id INTEGER PRIMARY KEY,
#     date TEXT NOT NULL,
#     product TEXT NOT NULL,
#     sales INTEGER, 
#     region Text
#     )  
# ''')   

# Insert the data in database
sales_date = [
    ('2025-01-01', 'Laptop', 1500, 'North'),
    ('2025-01-02', 'Smartphone', 800, 'South'),
    ('2025-01-03', 'Tablet', 600, 'East'),
    ('2025-01-04', 'Smartwatch', 300, 'West'),
    ('2025-01-05', 'Headphones', 200, 'North'),
    ('2025-01-06', 'Monitor', 400, 'South'),
    ('2025-01-07', 'Keyboard', 100, 'East'),
    ('2025-01-08', 'Mouse', 50, 'West'),
    ('2025-01-09', 'Printer', 250, 'North'),
    ('2025-01-10', 'Scanner', 150, 'South')
]

# Insert bulk data into the sales table
cur.executemany('''
INSERT INTO sales(date, product, sales, region)
            values (?,?,?,?)
''', sales_date)


# # Upadate the data in the table
# cur.execute('''
# UPDATE employee1
#         set age=34
#             where name = 'Nitish'
# ''')  


# # Delete the data in the table
# cur.execute('''
# DELETE from employee1
#             where name = 'Ravi'
# ''')  

conn.commit()  # it may sure that it really affect the database

# Retrieve the data from database
cur.execute('Select * from sales')
rows = cur.fetchall()

# Print the quiryed data
for t in rows:
    print(t)


cur.close()
conn.close()