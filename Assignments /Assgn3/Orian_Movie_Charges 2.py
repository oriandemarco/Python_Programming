# File:    Orian_Movie_Charges.py 
# Project: CSIS2101 Assignment 3
# Author:  Orian Demarco 
# History: Version 1.1 September 13, 2023
# Program: Calculate Total Movie Theater Charges.


print ("Hello,")
print ("I'm here to help you calculate your total movie theater charges for today.")
print (" ")
#I wanted to introduce what the purpose of this program is to the user.
#I also put a blank print function to make the outputs look cleaner. 
#I could have used \n if I wanted to put breaks within text, but I think this looks more organized.  

def Orian_Movie_Charges ():
#This is my main function which will be called at the end of code    
    
    TICKET_PRICE = 13.50
    SENIOR_DISCOUNT = 0.8 
    CONSESSIONS_DISCOUNT = 0.5
#I met with Brandon and he recommended to get in the practice of putting constants near the top, 
#of my code as this is not only required for other languages, but also makes code easier to understand. 

#Additionally I put these values in constants to make the code easier to read, and to give the 
#possibility of updating these values without any hassle if it were nessesary in the future. 

    num_of_adults_orian = int( input( "How many adults will be attending?: " ) )    
    num_of_seniors_orian= int( input( "How many senior citizens will be attending?: " ) )
#I followed the names instructed in the assignment rubric and created input statements instructing 
#the user what type of values they should input in each statement. 

    standard_ticket_rate =  TICKET_PRICE * (num_of_adults_orian - num_of_seniors_orian) 
    senior_ticket_rate = (TICKET_PRICE * SENIOR_DISCOUNT) * num_of_seniors_orian 
    total_ticket_price = standard_ticket_rate + senior_ticket_rate
#I chose variable names based upon the information being calculated. I purposely chose 
#to make the distinction between the use of price and the use of rate. Rate implies variability, in 
#this case, the amount of individuals vary and therefore influence the final pricing, making the first 
#two variables rates. Price is usually referred to a fixed value, the constant TICKET_PRICE is a
#given value and the name total_ticket_price implies the final calculation for the total cost of tickets

#Additionally, it was mentioned in our lecture that although seniors would be counted toward the total 
#amount of adults, they are to recieve their own discount for tickets. Because of this distinction in ticket 
#pricing, I created one variable for standard pricing and then one for senior pricing and added them together in a 
#seperate variable. The amount of seniors is relevant to total adults, but not relevant to stand pricing, so 
#I subtracted the amount of seniors from the first variable, and focused on seniors in the second variable


    if num_of_adults_orian < 4:
        cost_for_consessions= 10.75 * num_of_adults_orian
    elif num_of_adults_orian < 6:
        cost_for_consessions= 10.00 * num_of_adults_orian
    elif num_of_adults_orian < 8:
        cost_for_consessions= 8.50 * num_of_adults_orian   
    elif num_of_adults_orian < 10:
        cost_for_consessions= 7.25 * num_of_adults_orian  
    else:
        cost_for_consessions= 5.00 * num_of_adults_orian 
 #This is my if elif else function based on the consession table within the assignment sheet. Becuase the last condition 
 #given in the assignment was "greater than or equal to 10" I was able to put that pricing in the else statement 
 #because all conditions under a group of ten were previously covered in the lines above the else condition.

    total_theater_charges = total_ticket_price + cost_for_consessions
#I made this function that will take the total ticket price and add it with the total price for conssesions to
#give a total amount of theater charges

#I chose to put this here, instead of below the annual pass function, because I think it looks neater 
#considering I just covered both charges that are being added in the function 

    Annual_pass_holder = str ( input( "Are you an Annual Pass Holder? True or False: ") )
    if Annual_pass_holder == "True": 
        total_ticket_price = 0
        cost_for_consessions = cost_for_consessions * CONSESSIONS_DISCOUNT  
    elif Annual_pass_holder != "False": 
        print("Invalid Respnse. An invalid response is considered False. Please try again and enter True or False. "  )
#I first went ahead and asked the user if they have a pass by using a string input of True or False.
#If the statement is true, I updated the total ticket price to be free, and applied the consession's half off discount.
#If the statement inputed is anything other than false, hense the use of !=, I told the user their response is invalid, 
#mentioned that an invalid response is considered false, and reminded them what two responses are considered valid. 

        
     
    print (" ")
    print("Number of Adults: ", num_of_adults_orian)  
    print("Number of Seniors: ", num_of_seniors_orian) 
    print ("Annual Pass Holder: ", Annual_pass_holder)
    print (" ")
#I added 2 blank print functions to make the 3 outputs organized and easier to read.
#The 3 outputs are based upon the 3 orginal user inputs, with statements beforehand describing
#what each output statement above refers to. 


    print (f"Total Ticket Charges: ${total_ticket_price:0.2f}" )
    print (f"Total Consession Charges: ${cost_for_consessions:0.2f}" )
    print (f"Total Movie Theater Charges: ${total_theater_charges:0.2f}" )
#These 3 outputs are based upon the 3 final calculations specified in our assignment, 
#The printed statements beforehand describe what each output refers to, and I used the f string because 
#the calculated outputs are a currency, so they must be 2 decimal place values.

Orian_Movie_Charges ()
#Here, I called the main function, so the program could run. 