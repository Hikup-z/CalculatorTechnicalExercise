import math
import time as t

dash30 = "-"*30

#ask them what theyre converting from and to
#convert their input to denary
#convert denary to their desired output

def start():
    print(f"""
    {dash30}
    All-Purpose Calculator\n

    Which unit would you like to convert from?
    1. Decimal
    2. Binary
    3. Octal
    4. Hexadecimal

    (enter 0 to return to the main menu)
    {dash30}
    """)

    choice = int(input("Enter 1 / 2 / 3 / 4 : "))
    match (choice):
        case 1:
            decimalVersion = decimal_decimal()
        case 2:
            decimalVersion = binary_decimal()
        case 3:
            decimalVersion = octal_decimal()
        case 4:
            decimalVersion = hexadecimal_decimal()
        case 0:
            return None
        case _:
            print("Invalid Input")
            t.sleep(1)
            start()

    print(f"""
    {dash30}
    All-Purpose Calculator\n

    Which unit would you like to convert to??
    1. Decimal
    2. Binary
    3. Octal
    4. Hexadecimal

    (enter 0 to return to the main menu)
    {dash30}
    """)

    choice = int(input("Enter 1 / 2 / 3 / 4 : "))
    match (choice):
        case 1:
            print(f"Decimal: {decimalVersion}")
        case 2:
            decimal_binary(decimalVersion)
        case 3:
            decimal_octal(decimalVersion)
        case 4:
            decimal_hexadecimal(decimalVersion)
        case 0:
            return None
        case _:
            print("Invalid Input")
            t.sleep(1)
            start()




#conversions to denary ---------------------------
def decimal_decimal():
    value = int(input("Enter the value you would like to convert: "))
    #no calculations necessary
    return value

def binary_decimal():
    value = input("Enter the value you would like to convert: ")

    decimal = 0
    for digit in value:
        decimal = decimal*2 + int(digit)

    return decimal

def octal_decimal():
    value = input("Enter the value you would like to convert: ")

    valuearray = [*value]
    length = len(valuearray)
    decimal = 0
    #print(length)
    for i in valuearray:
        length -= 1
        #print(f"BEFORE i = {i}  - length = {length}  - decimal = {decimal}")
        decimal += (int(i) * 8**length)
        #print(f"AFTER i = {i}  - length = {length}  - decimal = {decimal}")
    
    return decimal
    


def hexadecimal_decimal():
    value = input("Enter the value you would like to convert: ")
    decimal = int(value, 16)
    return decimal

# -----------------------------------------------

#conversions from denary -------------------------

def decimal_binary(decimalVersion):
    binaryVersion = bin(decimalVersion)[2:]
    print(f"Binary: {binaryVersion}")
    t.sleep(1)
    start()

def decimal_octal(decimalVersion):
    octalVersion = oct(decimalVersion)[2:]
    print(f"Octal: {octalVersion}")
    t.sleep(1)
    start()

def decimal_hexadecimal(decimalVersion):
    hexadecimalVersion = hex(decimalVersion)[2:]
    print(f"Hexadecimal: {hexadecimalVersion}")
    t.sleep(1)
    start()

# -------------------------------------------------





