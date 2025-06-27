# Shop Database;

# Querises:
import sqlite3

conn = sqlite3.connect('Shop.db')
cur = conn.cursor()
rows = cur.execute('select Cname from Costumers')  


cur.close()
conn.close()