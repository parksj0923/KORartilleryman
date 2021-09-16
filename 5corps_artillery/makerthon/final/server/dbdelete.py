import sqlite3 as sql

con = sql.connect("database.db")
cur = con.cursor()

cur.execute("DELETE FROM mask") 
con.commit()
con.close()

