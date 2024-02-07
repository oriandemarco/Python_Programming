# File:    Orian_Movie_Charges.py 
# Project: CSIS2101 Assignment 3
# Author:  Orian Demarco 
# History: Version 1.1 September 13, 2023
# Program: Calculate Total Movie Theater Charges.


print ("Hello,")
print ("I'm here to help you calculate your total movie theater charges for today.")
print (" ")

def Orian_Movie_Charges ():  
    
    TICKET_PRICE = 13.50
    SENIOR_DISCOUNT = 0.8 
    CONSESSIONS_DISCOUNT = 0.5

    num_of_adults_orian = int( input( "How many adults will be attending?: " ) )    
    num_of_seniors_orian = int( input( "How many senior citizens will be attending?: " ) )

    standard_ticket_rate =  TICKET_PRICE * (num_of_adults_orian - num_of_seniors_orian) 
    senior_ticket_rate = (TICKET_PRICE * SENIOR_DISCOUNT) * num_of_seniors_orian 
    total_ticket_price = standard_ticket_rate + senior_ticket_rate


    if num_of_adults_orian < 4:
        cost_for_consessions = 10.75 * num_of_adults_orian
    elif num_of_adults_orian < 6:
        cost_for_consessions = 10.00 * num_of_adults_orian
    elif num_of_adults_orian < 8:
        cost_for_consessions = 8.50 * num_of_adults_orian   
    elif num_of_adults_orian < 10:
        cost_for_consessions = 7.25 * num_of_adults_orian  
    else:
        cost_for_consessions= 5.00 * num_of_adults_orian 
 

    Annual_pass_holder = str ( input( "Are you an Annual Pass Holder? True or False: ") )
    if Annual_pass_holder == "True": 
        total_ticket_price = 0
        cost_for_consessions = cost_for_consessions * CONSESSIONS_DISCOUNT  
    elif Annual_pass_holder != "False": 
        print("Invalid Respnse. An invalid response is considered False. Please try again and enter True or False. "  )
    
    total_theater_charges = total_ticket_price + cost_for_consessions
    
    print (" ")
    print("Number of Adults: ", num_of_adults_orian)  
    print("Number of Seniors: ", num_of_seniors_orian) 
    print ("Annual Pass Holder: ", Annual_pass_holder)
    print (" ") 


    print (f"Total Ticket Charges: ${total_ticket_price:0.2f}" )
    print (f"Total Consession Charges: ${cost_for_consessions:0.2f}" )
    print (f"Total Movie Theater Charges: ${total_theater_charges:0.2f}" )

Orian_Movie_Charges ()
