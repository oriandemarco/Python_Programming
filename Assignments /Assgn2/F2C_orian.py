# File:    F2C_Orian.py 
# Project: CSIS2101 Assignment 2
# Author:  Orian Demarco
# History: Version 1.1 September 8, 2023
# Program: Convert Temperatures from Celsius to Fahrenheit


print("Hello.")
print("I will convert temperatures from Fahrenheit to Celsius for you.")
#Here I introduced what I will be doing in a pleasant greeting. 
#I chose to put the hello print statement on its own line so it looks cleaner.

cel_orian = float(input("Please enter a temperature in Fahrenheit: "))
#I presented a useful prompt message that instructs the user what type of value they should input. 
#Using float, I converted this same input statement into a float so that it has a decimal value rather than a whole number.

T = 32
#Using a constant for 32 makes this code easier to construct, read, and prevents typos 

fahr_demarco = (cel_orian * 9/5) + t
#This is the conversion formula for Celsius to Fahrenheit

print (f"{cel_orian} degrees Celsius is equivelent to {fahr_demarco: .3f} degrees Fahrenheit.")
#I used an f string to format the output with placeholders for my variables.
#Speaking of format, I used .3f for the Fahrenheit variable so that my output would be rounded to 3 decimal places.

print ("Thank you.")
#I thought this was a nice touch at the end to be polite. 

