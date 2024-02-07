# File:    Assgn6_Orian.py 
# Project: CSIS2101 Assignment 6
# Author:  Orian Demarco 
# History: Version 1.2 October 13, 2023
# Program: Element Rock Paper Scissors AND Triangle Area.

import random
import math
                #Here I imported two modules, one for each of the programs in this assignment.
def main_orian():
    orian_choice = input("Enter your choice (Earth, Fire, or Water): ")
    valid_choices = ['Earth', 'Fire', 'Water']
                
    while orian_choice not in valid_choices:
            print("Invalid choice. Please enter Earth, Fire, or Water.")
            orian_choice = input("Enter your choice (Earth, Fire, or Water): ")
                # Here I called the main function ask the user for an input and then listed 
                # the valid choices. I also made a while loop in case the user doesn't provide 
                # a valid response that repeats until one is given. 

    random_number = random.randint(1, 9)
    if random_number <= 3:
        comp_choice = 'Earth'
    elif random_number <= 6:
        comp_choice = 'Fire'
    else:
        comp_choice = 'Water'
    
    EFW_orian(orian_choice, comp_choice)
                # Here I called a random number 1 to 9 then gave conditionals for the number
                # to be assigned to a specified element string value by using if-elif-else. 
                # And I called the function that determines the winning output statement 
                # for the EFW game.

    a, b, C = eval(input("Please enter sides a and b and angle C in degrees, separated by commas: "))
    is_valid_orian (a, b, C)
    compute_area_orian (a, b, C)
                # Here I ask the user the input for the 2nd program in the assignemnt 
                # and called the two main functions for this 2nd program.


def EFW_orian(orian_choice, comp_choice):
    print("Player Chose:", orian_choice)
    print("Computer Chose:", comp_choice)
    if orian_choice == comp_choice:
        print("Sorry, no winners as the game is a Tie.")
    elif orian_choice == 'Earth':
        if comp_choice == 'Fire':
            print("Computer wins as Fire burns Earth.")
        elif comp_choice == 'Water':
            print("Player wins as Earth absorbs Water.")
    elif orian_choice == 'Water':
        if comp_choice == 'Fire':
            print("Player wins as Water extinguishes Fire.")
        elif comp_choice == 'Earth':
            print("Computer wins as Earth absorbs Fire.")
    elif orian_choice == 'Fire':
        if comp_choice == 'Water':
            print("Player wins as Fire burns Water.")
        elif comp_choice == 'Earth':
            print("Computer wins as Earth absorbs Water.")
                # I used a nested if-elif statement to determine the winning outcome 
                # based on the two arguments, player and computer choice. 



def is_valid_orian(a, b, C):
    if a > 0 and b > 0 and 0 < C < 180:
        return True
    else:
        return False
    
while not is_valid_orian:
    print("Invalid input. Please make sure a and b are positive and 0 < C < 180.")    
    a, b, C = eval(input("Please enter two sides of a triangle and the included angle in degrees, separated by commas: "))


            # Here I specify the conditions for the users input and what will happen 
            # if the conditions are not met. The user will get an invalid input message, 
            # and be told what to enter until they meet the conditions.

def compute_area_orian(a, b, C):
    radians_C = math.radians(C)
    area = 0.5 * a * b * math.sin(radians_C)
    print(f"Area of the triangle with sides {a}, {b}, and included angle of {C} is {area:.2f} square inches.")

            # Here I compute the area of the given parameters with the help of the math 
            # module, and then print the result using the f string as placeholders and 
            # aslo inserted the 2 decimal place format for the area. 
main_orian()
            # Here I call the main function.

