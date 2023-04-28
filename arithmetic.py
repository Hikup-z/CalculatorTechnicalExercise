
#module imports
import time as t
import math as m


dash30 = "-"*30
numbers = []


def start():
    print(f"""
    {dash30}
    All-Purpose Calculator\n

    Enter a mathematical expression using the following operators:

    + for addition
    - for subtraction
    * for multiplication
    / for division

    (enter 'exit' to return to the main menu)
    {dash30}

    """)

        
    while True:
        expression = input("Input:   ")

        if expression == "exit":
            return None
        else:
            pass

        #need validation to make sure only symbols and numbers are inputted 
        #would stop the program from running malicious code
        #also allows me to send back to main menu if the user inputs something invalid

        expression = expression.replace(" ", "")
        expressionList = [*expression]

        for i in expressionList:
            if i.isalpha() == False and i.isdigit() == False and i != "+" and i != "-" and i != "*" and i != "/" and i != "." and i != "(" and i != ")":
                print("Invalid Input")
                t.sleep(1)
                return None
                
            else:
                pass

        print(f"Answer: {round(eval(expression), 2)}")

        

                    
        


