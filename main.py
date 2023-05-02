#file imports
import conversions
import arithmetic
import computerConversions

#module imports
import time as t
import math as m
import sys

#plan: main menu, user can choose between arithmetic operations or unit conversions
# arithmetic user can choose between console input or selection from a list
#



dash30 = "-"*30

def mainMenu():
    print(f"""
    {dash30}
    All-Purpose Calculator\n

    1. Arithmetic Operations
    2. Unit Conversions
    3. Computer Unit Conversions\n

    (enter 0 to exit the program) 
    {dash30}


    """)
    try:
        choice = int(input("Enter 1 / 2 / 3: "))
        

    except ValueError: #used w3schools, couldnt remember the syntax for the try except statement
        print("Invalid Input")
        t.sleep(1) #using sleep statements so that the user can see the output clearly, stops the console jumping around
        mainMenu()

    t.sleep(1)
    
    match (choice): 
        case 1: 
            call_arithmetic()
        case 2:
            call_conversions()
        case 3:
            call_otherConversions()
        case 0:
            print("Exiting Program")
            t.sleep(1)
            sys.exit()
    
        case _:
            print("Invalid Input")
            t.sleep(1)
            mainMenu()

def call_arithmetic():
    if arithmetic.start() == None:
        mainMenu()

    

def call_conversions():
    if conversions.start() == None:
        mainMenu()

def call_otherConversions():
    if computerConversions.start() == None:
        mainMenu()
                

mainMenu()


# Problems / Discussions:

# The user has to enter 0 twice to return to main menu from the arithmetic and conversion, havent yet figured out why
# realised it was because i was calling the start function twice, one to call it originally and again to check if its equal to None:

#arithemtic.start()
# if arithmetic.start() == None:
#     mainMenu()

