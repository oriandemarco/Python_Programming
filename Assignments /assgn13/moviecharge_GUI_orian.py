# File:    moviecharge_GUI_orian.py 
# Project: CSIS2101 Assignment 13
# Author:  Orian Demarco 
# History: Version 1.1 November 28, 2023
# Program: GUI for "Calculate Total Movie Price" Assignment.

import tkinter

class Movie_orian:
    def __init__( self ):
        self.main_window = tkinter.Tk()
        self.main_window.title("MOVIE TRIP PRICE CALCULATOR")
        self.frame1_orian = tkinter.Frame( self.main_window )
        self.frame2_orian = tkinter.Frame( self.main_window )
        self.frame3_orian = tkinter.Frame( self.main_window ) 
        self.frame4_orian = tkinter.Frame( self.main_window )
        self.frame5_orian = tkinter.Frame( self.main_window )
        self.frame6_orian = tkinter.Frame( self.main_window )
    

            # movie ticket price 
        self.t_price_prompt_label = tkinter.Label( self.frame1_orian,text = "Please enter the price for the movie:", borderwidth = 2, relief = "ridge" )
        self.t_price_entry = tkinter.Entry( self.frame1_orian, width = 15 ) 
                            

        self.t_price_prompt_label.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )
        self.t_price_entry.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )
                            # I first put the title and set each of the frames up. 4 of the frames have labels with descriptive text boxes
                            # and entry fields for the user to input their responses. I packed each widget inside each frame.  
                            # I also experimented with borderwidth, relief setting, entry box width, and inside and outside padding


            # number of adults 
        self.adult_prompt_label = tkinter.Label( self.frame2_orian,text = "Please enter the amount of adults, including seniors:", borderwidth = 2, relief = "ridge" )
        self.adult_entry = tkinter.Entry( self.frame2_orian, width = 15 )

        self.adult_prompt_label.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )
        self.adult_entry.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )


            # number of seniors 
        self.senior_prompt_label = tkinter.Label( self.frame3_orian,text = "Please enter the amount of seniors:", borderwidth = 2, relief = "ridge" )
        self.senior_entry = tkinter.Entry( self.frame3_orian, width = 15 )

        self.senior_prompt_label.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )
        self.senior_entry.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )


            # annual pass holder  
        self.p_holder_prompt_label = tkinter.Label( self.frame4_orian,text = "Are you an Annual Pass holder? True or False:", borderwidth = 2, relief = "ridge")
        self.p_holder_entry = tkinter.Entry( self.frame4_orian, width = 15 )

        self.p_holder_prompt_label.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )
        self.p_holder_entry.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30 )

            # total price calculated 
        self.descr_label = tkinter.Label( self.frame5_orian,text = "Total Price:", borderwidth = 6, relief = "ridge" )
        self.value = tkinter.StringVar()
        self.total_price_label = tkinter.Label( self.frame5_orian, textvariable = self.value )
        self.descr_label.pack( side = "left", ipadx = 15, ipady = 15, padx = 30, pady = 30)
        self.total_price_label.pack(side = "left")
                            # I used StringVar to correspond with the output label so 
                            # it can update when needed 

            # calculate and quit buttons 
        self.calc_button = tkinter.Button( self.frame6_orian, text = "CALCULATE", command = self.calc_movie_charge_orian )
        self.quit_button = tkinter.Button( self.frame6_orian, text = "QUIT", command = self.main_window.destroy )
                            # the calc movie charge function is called for when the user clicks the button

        self.calc_button.pack(side = "left", ipadx = 30, ipady = 30, padx = 30, pady = 30)
        self.quit_button.pack(side = "left", ipadx = 30, ipady = 30, padx = 30, pady = 30)  

        self.frame1_orian.pack()  
        self.frame2_orian.pack()
        self.frame3_orian.pack()
        self.frame4_orian.pack()
        self.frame5_orian.pack()
        self.frame6_orian.pack()
        tkinter.mainloop()
                            # packed the frames and called the event loop 

    def calc_movie_charge_orian (self):
        SENIOR_DISCOUNT = 0.8 
        CONSESSIONS_DISCOUNT = 0.5

        ticket_price = float (self.t_price_entry.get())
        num_of_adults = float (self.adult_entry.get())
        num_of_seniors = float (self.senior_entry.get())
        annual_pass_holder = (self.p_holder_entry.get())
                            # get the values from user's inputs

        standard_ticket_rate =  ticket_price * (num_of_adults - num_of_seniors) 
        senior_ticket_rate = (ticket_price * SENIOR_DISCOUNT) * num_of_seniors 
        total_ticket_price = standard_ticket_rate + senior_ticket_rate

        if num_of_adults < 4:
            cost_for_consessions = 15.75 * num_of_adults
        elif num_of_adults < 6:
            cost_for_consessions = 15.00 * num_of_adults
        elif num_of_adults < 8:
            cost_for_consessions = 8.50 * num_of_adults 
        elif num_of_adults < 15:
            cost_for_consessions = 7.25 * num_of_adults
        else:
            cost_for_consessions= 5.00 * num_of_adults 
    
        if annual_pass_holder == "True": 
            total_ticket_price = 0
            cost_for_consessions *= CONSESSIONS_DISCOUNT  
        elif annual_pass_holder != "False": 
            self.value.set("Invalid Respnse. An invalid response is considered False. Please try again and enter True or False." )
            return 
            
        total_theater_charges = total_ticket_price + cost_for_consessions
        self.value.set("${:.2f}".format(total_theater_charges))
                        # I considered if the user entered something other than true or false 
                        # and set the value to a statement that informs them. I then created the total charges variable 
                        # and formated it for the GUI
if __name__ == "__main__":
    calc = Movie_orian()
