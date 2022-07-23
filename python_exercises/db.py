from dotenv import load_dotenv

import sqlite3

# with context require no commit and close
# with sqlite3.connect("testdb.db") as connection:

# with sqlite3.connect(":memory:") as connection:

connection = sqlite3.connect("testdb.db")

cursor = connection.cursor()

# cursor.execute('CREATE TABLE User (name TEXT, age INT);')

name = "funmi"
age = 52

cursor.execute("INSERT INTO User VALUES (?, ?)", (name, age))

# cursor.executemany()
# cursor.executescript()
users = (('florence', 35), ('Ademola', 42), ('Amaka', 20))

cursor.executemany("INSERT INTO User VALUES (?, ?)", users)
cursor.execute("SELECT * FROM User;")

print(cursor.fetchall())

connection.commit()

connection.close()
