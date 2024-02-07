# File:    menu_orian.py 
# Project: CSIS2101 Assignment 7
# Author:  Orian Demarco 
# History: Version 1.2 October 23, 2023
# Program: Planet Weight Conversion Menu.

import weights_orian
K = 2.2
                    # I first imported the weights file and defined the constant K for mass to kilograms
def valid_input_orian(mass, units):
    mass = float(mass)
    if mass > 0 and units == "lbs":
        return True 
                    # Idefined the valid input function, which takes in parameters of mass and units, 
                    # then changed mass into a float value before checking the given conditions required for
                    # it to return true, and therefore, be validated

def menu_demarco():
    print("MENU")
    print("a) Weight of an object in Newtons on Moon.")
    print("b) Weight of an object in Newtons on Earth.")
    print("c) Weight of an object in Newtons on Mars.")
    print("d) Weight of an object in Newtons on Saturn.")
    print("e) Exit the program.")
                    # Here I wrote a void method to display the menu 
def main():
    print(" ")
    menu_demarco()
    print(" ")
    menu_choice = input("Enter your menu choice: ")
                    # I defined main then put some print statements around the menu for output readability
                    # then I ask the user to input their menu menu_choice
    while menu_choice != "e":
        if menu_choice == "a":
            print("We are going to calculate the weight of the object on Moon")
            print(" ")
            mass = int(input("Please enter the mass of the object: "))
            units = input("Please enter the corresponding units: ")
            while not valid_input_orian(mass, units):
                print("Mass entered is negative or/and Invalid Units for weight. It should be lbs.")
                print(" ")
                mass = int(input("Please enter the mass of the object: "))
                units = input("Please enter the corresponding units: ")
            mass_kg = mass / K
            weight_moon = weights_orian.weight_moon_orian(mass_kg)
            print(f"Weight of the object with a mass of {mass:.3f} pounds: {weight_moon:.3f} Newtons on Moon")
            main()
                    # I used a while loop to give instructions for each input aside from e. For each option I tell the user 
                    # what we're going to calculate based on their menu menu_choice then put a print statement for readability. 
                    # I then ask the user for their mass and unit input. Then I validate the mass and units by using a while loop 
                    # with valid_input which will check for the met conditions. The while loop allows the output (which tells the user
                    # their input is wrong and asks for the mass and unit inputs again) to run over and over until condition are met. 
                    # Once the input is validated, I then convert the inputted mass to kilogram using the constant defined in the top
                    # of this assignemnt. Next, the mass in kg is multiplied by each planets gravity, specified in the weights file. 
                    # Then, I print the final answer using an f statement and .3 formating for both the original inputed mass and the 
                    # weight in newtons. Finally, I call the main function to make the menu display again and repeat the whole 
                    # program for a new input. I repeat these steps for each of the 3 planets below.
        elif menu_choice == "b":
            print("We are going to calculate the weight of the object on Earth")
            print(" ")
            mass = int(input("Please enter the mass of the object: "))
            units = input("Please enter the corresponding units: ")
            while not valid_input_orian(mass, units):
                print("Mass entered is negative or/and Invalid Units for weight. It should be lbs.")
                print(" ")
                mass = int(input("Please enter the mass of the object: "))
                units = input("Please enter the corresponding units: ")
            mass_kg = mass / K  
            weight_earth = weights_orian.weight_earth_orian(mass_kg)
            print(f"Weight of the object with a mass of {mass:.3f} pounds: {weight_earth:.3f} Newtons on Earth")
            main()
        elif menu_choice == "c":
            print("We are going to calculate the weight of the object on Mars")
            print(" ")
            mass = int(input("Please enter the mass of the object: "))
            units = input("Please enter the corresponding units: ")
            while not valid_input_orian(mass, units):
                print("Mass entered is negative or/and Invalid Units for weight. It should be lbs.")
                print(" ")
                mass = int(input("Please enter the mass of the object: "))
                units = input("Please enter the corresponding units: ")
            mass_kg = mass / K  
            weight_mars = weights_orian.weight_mars_orian(mass_kg)
            print(f"Weight of the object with a mass of {mass:.3f} pounds: {weight_mars:.3f} Newtons on Mars")
            main()
        elif menu_choice == "d":
            print("We are going to calculate the weight of the object on Saturn")
            print(" ")
            mass = int(input("Please enter the mass of the object: "))
            units = input("Please enter the corresponding units: ")
            while not valid_input_orian(mass, units):
                print("Mass entered is negative or/and Invalid Units for weight. It should be lbs.")
                print(" ")
                mass = int(input("Please enter the mass of the object: "))
                units = input("Please enter the corresponding units: ")
            mass_kg = mass / K  
            weight_saturn = weights_orian.weight_saturn_orian(mass_kg)
            print(f"Weight of the object with a mass of {mass:.3f} pounds: {weight_saturn:.3f} Newtons on Saturn")
            main()
        else:
            print("Invalid Menu choice. Please pick a valid choice.")
            main()
                    # this last option prints a statement for any input given that isn't listed on the menu
                    # I then call main so the program can repeat and the user can see the menu and pick a valid option.
    if menu_choice == "e":
            print("Good Bye to the Weight calculator!")
            print(" ")
                    # I put menu_choice e in its own if statement so the program exits once given the input e, unlike all other options.
main()
                    #called the main function
