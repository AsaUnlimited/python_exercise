import sqlite3

firstName = input("Enter your first name: ")
age = int(input("Enter your age: "))

user_info = (firstName, age)

with sqlite3.connect("testdb.db") as connect_user:
    cursor = connect_user.cursor()
    cursor.execute("INSERT INTO USer VALUES (?, ?)", user_info)
    cursor.execute("SELECT * FROM User")
    print(cursor.fetchall())