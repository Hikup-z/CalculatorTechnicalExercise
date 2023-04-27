#module imports
import time as t
import math as m

dash30 = "-"*30

def start():
    print(f"""
    {dash30}
    All-Purpose Calculator\n

    1. Console Entry
    2. Selection from List\n
    {dash30}

    """)
    try:
        choice = int(input("Enter 1 / 2 : "))
    except ValueError:
        print("Invalid Input")
        t.sleep(1)
        start()
    match (choice):
        case 1:
            console_entry()
        case 2:
            list_entry()
    
def console_entry():
    pass

def list_entry():
    pass