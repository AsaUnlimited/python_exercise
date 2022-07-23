import sqlite3

connection = sqlite3.connect("test_database.db")
# print(type(connection))

cursor = connection.cursor()
# print(type(cursor))

query = "SELECT datetime('now', 'localtime');"
cursor.execute(query)
time = cursor.execute(query).fetchone()[0]
print(time)

# connection.close()

with sqlite3.connect("testtdb.db") as connect:
    cursor = connect.cursor()
    q = "SELECT datetime('now', 'localtime');"
    t = cursor.execute(q).fetchone()[0]

print(t)

with sqlite3.connect("testtdb1.db") as connect:
    cursor = connect.cursor()
    # cursor.execute(
    #     """
    #     CREATE TABLE people(
    #         FirstName TEXT,
    #         LastNAme TEXT,
    #         Age INT
    #     );"""
    # )
    #
    # cursor.execute("""
    #     INSERT INTO people VALUES (
    #         'Asa',
    #         'Obvious',
    #         42
    #     );"""
    #   )

    connect.commit()

    cursor.execute("SELECT * FROM people;")
    print(cursor.fetchone())