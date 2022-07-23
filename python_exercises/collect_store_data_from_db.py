import sqlite3

fullname = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
dob = int(input("Enter your date of birth"))

user_info = (fullname, email, phone, dob)

with sqlite3.connect("userdb", ) as userdb:
    cursor = userdb.cursor()
    try:
        cursor.execute("INSERT INTO USER VALUES(?, ?, ?, ?)", user_info)
    except:
        userdb.rollback()
