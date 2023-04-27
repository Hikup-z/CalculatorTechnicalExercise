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
    pass

def gigabytes_bytes():
    pass

def inches_centimetres():
    pass

def days_seconds():
    pass