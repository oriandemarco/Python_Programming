# File:    for_while_loop_orian.py 
# Project: CSIS2101 Assignment 4
# Author:  Orian Demarco 
# History: Version 1.2 September 25, 2023
# Program: Basic Loops.

def for_while_loop_orian () :
         # Assignmet part 1 
     counter_orian = -99
     while counter_orian >= -112:
        print(counter_orian, end= " &") 
        counter_orian -= 1
     print ("-113&")
      
         # This loop counts down from -99 to -113 and prints each value on 
         # the same line separtated by & signs.
         # Becasue I'm using a while loop, I specified the counter starts at -99.
         # The formating of my print statement allows for the outputs to all print 
         # on the same line and allow for the & sign to be spaced accordingly.
         # The updated counter at the end allows the values of each output to descrease.

         # I had a bit of confusion on the ending of this question because on the aissignment, 
         # all numbers in the output have spaces in front of each & sign aside from the last "113&"
         # On this number there is no space before the & sign and I'm not sure if this was a typo or not.
         # In my work above, I'm assuming it was a typo, but if it was meant to be like that, 
         # I would set while counter_orian on line 10 to -112 intead of -113 and I would put a print 
         # "-113&" on line 13, alined with the start of the while loop, not nested inside it.
    
    
     print (" ")
     print (" ")
         # These print statements are just for the visual appearence of the output.

         # Assignment part 2
     orian = 0
     for orian in range (0, 169, 13):
      if orian % 13 == 0 and orian % 3 != 0:
       print(orian, end=", ")
     print ("169")
         # This loop counts from 0 to 169 by 13s, printing the count in each 
         # iteration but omitting numbers that are divisible by both 13 and 3.
         # I started by defining my name variable before starting the loop.
         # I put the start end and step in the for statement then specified the 
         # conditional of being divisible by 13 and 3 using an if statement  
         # I formated the printing to all be on the same line using end= as I did in prior 
         #assignemnt part.
         # 169 was printed inependently for foratting reasons, to allow no comma at the end of the number.

         # This print statement is just for the visual appearence of the output.
     print (" ")

         # Assignemnt part 3
     n = int(input("Enter the number of questions on the assignment: "))

     for k in range(1, n):
      print(f"I answered question number {k}.")

     print(f"I am answering question number {n}.")

         # I started by asking the user to enter an integer number for the amount of questions.
         # I used a for loop to represent the range of questions and put the print statement bellow the range
         # as the only parameter so it'll print the history of questions answered.
         # The last rpint statement represents the current question the user is on, the same value as the 
         # # original input.
         # Both print statements utilize an f statment to allow placeholders before the periods for the values.    

         # This print statement is just for the visual appearence of the output.
     print (" ")



         #Assignment part 4 
     num1_orian = int(input("Enter the first number: "))
     num2_orian = int(input("Enter the second number: "))

     if num1_orian % 2 != 0:
      num1_orian += 1

     if num2_orian < num1_orian:
      while num1_orian > num2_orian:
        print(num1_orian, end=" ")
        num1_orian -= 2
     else:
      while num1_orian < num2_orian:
        print(num1_orian, end=" ")
        num1_orian += 2
print(" ")
         # I first asked the user to input two integer parameters, named as num1_orian and num2_orian.
         # I then used the first if statement to check if num1_orian is odd, 
         # if so, the program will start with the next even number.
         # In the second if statement I checked if num2_orian is less than num1_orian,
         # and dpending on such, it will count up or down from the first input num1_orian.
         # Lastly I wanted to add another print statement just to make output formating visually appealing
for_while_loop_orian()
         # I called the main function to perform all 4 elements.










