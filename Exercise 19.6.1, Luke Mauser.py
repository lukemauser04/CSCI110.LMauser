
import os

def posint():
    try:
        
        positive_integer = input("Please input a positive integer. ")
        if positive_integer.strip() == '':
            return ("No input was provided, please enter a valid positive integer. ")
                positive_integer = int(positive_integer)
        if positive_integer < 0:
            return("{0} is not a valid positive integer".format(positive_integer))   
        else:
            print("The input meets the requirements.", + positive_integer, "is a positive integer. Thank you!")
            
        
    except ValueError:
        print("The input provided was not an integer, please provide a positive integer for the input. ")
    
output = posint()
print(output)
