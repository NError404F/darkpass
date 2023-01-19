import os
import sys
import colorama
from termcolor import colored, cprint
import sqlite3

colorama.init()

#Enter db name with .db extension
db = ""
#Enter tb name
tb = ""

text = """
██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██║  ██║███████║██████╔╝█████╔╝ ██████╔╝███████║███████╗███████╗
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔═══╝ ██╔══██║╚════██║╚════██║
██████╔╝██║  ██║██║  ██║██║  ██╗██║     ██║  ██║███████║███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝                                                               
"""

connection = sqlite3.connect(db)
cursor =  connection.cursor()

def main():
    os.system("cls||clear")
    cprint(text, 'green')
    cprint("My github: https://github.com/NError404F", 'cyan')
    cprint("""
          [1] Add accout
          [2] View accounts
          [3] Delete account
          """, 'green')
    option = input("What do you want to do: ")
    if option == "1":
        addpass()
    elif option == "2":
        viewpass()
    elif option == "3":
        delacc()
    else:
        cprint("Invalid option...", 'red')
        os.system("timeout 3")
    

def addpass():
    os.system("cls||clear")
    name = input("Enter service name: ")
    username = input("Enter account username: ")
    password = input("Enter account password: ")
    
    cursor.execute(f"insert into {tb}(name, username, password) values('{name}', '{username}', '{password}')")
    connection.commit()

def viewpass():
    viewaccs = cursor.execute(f"select * from {tb}")
    print(cursor.fetchall())
    
    back = input("Type bk to go back to main menu: ")
    if back == "bk":
        main()
    else:
        cprint("Invalid input...", 'red')
        os.system("timeout 3")
        
def delacc():
    nametodel = input("Enter the service name you want to delete: ")
    sure = input("Are you sure you want to delete this service? [Y/N]: ")
    if sure == "Y":
        cursor.execute(f"delete from {tb} where name='{nametodel}'")
    elif sure == "N":
        main()
    else:
        cprint("Wrong input you focking donut, use capital letters!", 'red')
        os.system("timeout 5")
        main()


while True:
    main()
    

connection.close()