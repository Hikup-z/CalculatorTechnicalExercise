import time as t
import math as m

dash30 = "-"*30


def start():
    print(f"""
    {dash30}
    All-Purpose Calculator\n

    Which conversion would you like to perform?
    1. Kilos <--> Stone
    2. Gigabytes <--> Bytes
    3. Inches <--> Centimetres
    4. Days <--> Seconds

    {dash30}
    """)
    try:
        choice = int(input("Enter 1 / 2 / 3 / 4 : "))
    except ValueError:
        print("Invalid Input")
        t.sleep(1)
        start()
    match (choice):
        case 1:
            kilos_stone()
        case 2:
            gigabytes_bytes()
        case 3:
            inches_centimetres()
        case 4:
            days_seconds()

def kilos_stone():
    try :
        direction = input("Enter 1 to convert from kilos to stone, or 2 to convert from stone to kilos: ")
    except ValueError:
        print("Invalid Input")
        t.sleep(1)
        kilos_stone()

    match (direction):
        case "1":
            kilos = float(input("Enter the amount of kilos: "))
            stone = kilos / 6.35029318
            print(f"{kilos} kilos is equal to {round(stone, 2)} stone")

        case "2":
            stone = float(input("Enter the amount of stone: "))
            kilos = stone * 6.35029318
            print(f"{stone} stone is equal to {round(kilos, 2)} kilos")

        case "quit"

        case _:
            print("Invalid Input")
            t.sleep(1)
            kilos_stone()


def gigabytes_bytes():
    try:
        direction = input("Enter 1 to convert from gigabytes to bytes, or 2 to convert from bytes to gigabytes: ")
    except ValueError:
        print("Invalid Input")
        t.sleep(1)
        gigabytes_bytes()
    
    match (direction):
        case "1":
            gigabytes = float(input("Enter the amount of gigabytes: "))
            bytes = gigabytes * 1024 * 1024 * 1024
            print(f"{gigabytes} gigabytes is equal to {round(bytes, 2)} bytes")

        case "2":
            bytes = float(input("Enter the amount of bytes: "))
            gigabytes = bytes / 1024 / 1024 / 1024
            print(f"{bytes} bytes is equal to {round(gigabytes, 2)} gigabytes")

        case _:
            print("Invalid Input")
            t.sleep(1)
            gigabytes_bytes()
            

def inches_centimetres():
    try:
        direction = input("Enter 1 to convert from inches to centimetres, or 2 to convert from centimetres to inches: ")
    except ValueError:
        print("Invalid Input")
        t.sleep(1)
        inches_centimetres()

    match (direction):
        case "1":
            inches = float(input("Enter the amount of inches: "))
            centimetres = inches * 2.54
            print(f"{inches} inches is equal to {round(centimetres, 2)} centimetres")
        case "2":
            centimetres = float(input("Enter the amount of centimetres: "))
            inches = centimetres / 2.54
            print(f"{centimetres} centimetres is equal to {round(inches, 2)} inches")
        case _:
            print("Invalid Input")
            t.sleep(1)
            inches_centimetres()
       
def days_seconds():
    try:
        direction = input("Enter 1 to convert from days to seconds, or 2 to convert from seconds to days: ")
    except ValueError:
        print("Invalid Input")
        t.sleep(1)
        days_seconds()
    
    #turn the followiing if chain into a match case statement
    
    match (direction):

        case "1":
            days = float(input("Enter the amount of days: "))
            seconds = days * 86400
            print(f"{days} days is equal to {round(seconds, 2)} seconds")
        case "2":
            seconds = float(input("Enter the amount of seconds: "))
            days = seconds / 86400
            print(f"{seconds} seconds is equal to {round(days, 2)} days")
        case _:
            print("Invalid Input")
            t.sleep(1)
            days_seconds()
        
    