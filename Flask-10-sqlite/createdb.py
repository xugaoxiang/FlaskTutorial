import sqlite3

con = sqlite3.connect("users.db")
con.execute(
    "create table user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)")

print("Table created successfully!")
con.close()
