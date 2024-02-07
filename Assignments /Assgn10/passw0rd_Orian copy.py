# File:    passw0rd_Orian.py 
# Project: CSIS2101 Assignment 10
# Author:  Orian Demarco 
# History: Version 1.1 November 10, 2023
# Program: Input and Output Files.


import passwd 

def main():
    with open ("passwdin.txt", "r") as in_file:
        with open("orian_good_psswd_out.txt", "w") as good_output_file, open("orian_bad_psswd_out.txt", "w") as bad_output_file:
            line = in_file.readline()
                            # Here I specify the input file and output files then read the first line, line 13 is also my coutner for the while loop.  
            while line !="":
                password = line.strip("\n")
                            # here I first put a while loop which will run while there isn't an empty string. 
                            # I then strip the new line character and am left with password. 
                valid, message = passwd.check_password_Orian(password)
                if valid:
                    good_output_file.write(f"{password} - {message}\n")
                else:
                    bad_output_file.write(f"{password} - Password is not accepted.\n{message}\n")
                line = in_file.readline()
                            # Here I specify the location of the passwords depending on 
                            # if they meet the criteria listed in my passwd function check_password_orian. The results on whether
                            # or not the password is valid is pronted along with the message why if nessessary. 
                            # I then use readline on line 24 as the update counter.
if __name__ == "__main__":
    main()

