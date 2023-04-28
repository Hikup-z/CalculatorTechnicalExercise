#file imports
import conversions
import arithmetic

#module imports
import time as t
import math as m

#plan: main menu, user can choose between arithmetic operations or unit conversions
# arithmetic user can choose between console input or selection from a list
#



dash30 = "-"*30

def mainMenu():
    print(f"""
    {dash30}
    All-Purpose Calculator\n

    1. Arithmetic Operations
    2. Unit Conversions\n

    (enter 'exit' to return to the main menu)
    {dash30}


    """)
    try:
        choice = int(input("Enter 1 / 2 : "))

    except ValueError: #used w3schools, couldnt remember the syntax for the try except statement
        print("Invalid Input")
        t.sleep(1) #using sleep statements so that the user can see the output clearly, stops the console jumping around
        mainMenu()

    t.sleep(1)
    
    #need an exit statement here

    match (choice): #i prefer this to if elif else, makes the code look cleaner in my opinion
        case 1: 
            call_arithmetic()
        case 2:
            call_conversions()

def call_arithmetic():
    arithmetic.start()
    if arithmetic.start() == None:
        mainMenu()

    

def call_conversions():
    conversions.start()
    if conversions.start() == None:
        mainMenu()
                

mainMenu()