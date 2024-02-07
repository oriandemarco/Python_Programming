# File:    Assgn5_Orian.py 
# Project: CSIS2101 Assignment 5
# Author:  Orian Demarco 
# History: Version 1.2 October 2, 2023
# Program: Void Returning Functions with Parameters.

def main ():
 
 # Number 1          
 def orian_nested_loop(n):
   row_sum = 0
   for i in range(1, n+1):
      row_sum += i
      print(row_sum)
            # Here, I calculate the cumulative sum of numbers from 1 to the current row number using a nested loop. 
            # The loop iterates from 1 to n (n being the users input) and for each iteration, it adds the current 
            # row number to the cumulative sum. Then, the cumulative sum is then printed for each row.
 n = int(input("Enter number of rows: "))
 orian_nested_loop(n)
 print(" ")
            # Here, I called the function, then added a print sign for output readability.


 # Number 2   
 def sum_of_even_numbers_orian(x, y):
    total = 0
    for num in range(x, y, 2):
       total += num
    return total
            # Here I made a continuation of the 4th loop from the last assignment that adds the values that 
            # were printed. I started by defining the function and putting x and y as arguments. In the definition 
            # I first set total to zero. I then used a for loop that includes the numbers between the inputted x and 
            # y values. I also set the step to 2 so only even numbers are considered. I then set the total to add the 
            # numbers in the range and used a return so this process could be repeated for each number in the range. 

 x = int(input("Enter the first number: "))
 y = int(input("Enter the second number: "))
            # Here, I ask the user to input the integer values for x and y.
 while y <= x:
    print("Invalid input. The second number must be greater than the first number.")
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    sum_of_even_numbers_orian
            # Here, I put a loop to consider what will happen when y is less than or equal to x. I first tell the user
            # that their input is invalid and tell them what needs to be inputted. I then ask them to input the
            # 2 values again and repeat the loop.

 if x % 2 != 0:
        x += 1
            # Here, I consider if the inputted value of x is an odd number. If so, a 1 will be added to x
            # and the updated value will be saved.
            
 print (sum_of_even_numbers_orian (x, y)) 
 print(" ")
            # Here, I called the function, then added a print sign for output readability.


 # Number 3
 def orian_nursery_rhyme(device, property):
    print(f"Old MacDonald had a Computer, 1-0-1-0-1")
    print(f"And on his computer he had a {device}, 1-0-1-0-1")
    print(f"With a \"{property}-{property}\" here and a \"{property}-{property}\" there")
    print(f"Here a \"{property}\", there a \"{property}\"")
    print(f"Everywhere a \"{property}-{property}\"")
    print(f"Old MacDonald had a Computer, 1-0-1-0-1")
    print((" "))
            # Here, I formatted the song using print statements and f to keep the placeholders 
            # of the specified values of device and property. The / was used to allow the "" 
            # to be placed around the properties. I also added a blank print statement to 
            # organize each stanza. I debated using device/property strings speaker/sound 
            # or printer/print but ultimately chose keyboard/type and screen/tap.

 orian_nursery_rhyme("mouse", "click")
 orian_nursery_rhyme("keyboard", "type")
 orian_nursery_rhyme("screen", "tap")
            # Here, I called the nursery function with different string values in each.
main ()
            # Here, I called the main function with all 3 functions firstname_nested_loop, 
            # sum_even_numbers_firstname and firstname_nursery_rhyme nested inside.

