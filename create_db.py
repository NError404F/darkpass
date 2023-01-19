import sqlite3

dbname = input("Enter db name: ")
tbname = input("Enter table name (name of the table where the passwords are going to be stored): ")

connection = sqlite3.connect(f"{dbname}.db")
cursor =  connection.cursor()

cursor.execute(f"create table {tbname}(name , username , password)")

connection.close()