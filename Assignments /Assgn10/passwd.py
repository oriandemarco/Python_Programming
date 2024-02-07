# File:    passwd.py 
# Project: CSIS2101 Assignment 10
# Author:  Orian Demarco 
# History: Version 1.1 November 10, 2023
# Program: Input and Output Files.

def main():
    print( "A password is accepted if the following conditions are true: ")

    print("#1. Password is at least 12 characters long")
    print("#2. Password contains at least 2 lower case characters.")
    print("#3. Password contains 2 upper case characters.")
    print("#4. Password contains 2 digits.")
    print("#5. Password contains at least 2 special characters.")
    print("#6. Password contains no spaces.")
    print("#7. Password does not contain the upper case first letter of your first name or lower case second leter of your first name.")
    psswd = input( "Please enter a password: " )
                    # Here I just modified the printed password criteria that needs to be met by the user, then ask for a password input. 
    
    result, msg = check_password_Orian(psswd)

    if result:
        print(msg)
    else:
        print( "Password failed to meet following condition(s)\n", msg)
                    # I then saved the password check function, which takes in the users input, into result and msg to determin
                    # whetehr the password is validated or not, tell the user the result, and explain the reasoning if nessessary.


def check_password_Orian( pss ):
    lng = len( pss )
    lc_count = 0
    uc_count = 0
    dig_count = 0
    sp_ch_count = 0
    sp_count = 0

    first_name = "Orian"
    first_let = first_name[0].upper()
    second_let = first_name[1].lower()
                    # I took the program we did in class and modified it a bit. The set counts are still the same of course
                    # but I also added my name as a variable along with the indexes of the first two letters (O and r) to check if 
                    # those are used in the passwords. 

    for ch in pss:
        if ch.islower():
            lc_count += 1
        elif ch.isupper():
            uc_count += 1
        elif ch.isdigit():
            dig_count += 1
        elif ch.isspace():
            sp_count += 1
        else:
            sp_ch_count += 1

    if lng >= 12 and lc_count >= 2 and uc_count == 2 and dig_count == 2 and sp_count == 0 and sp_ch_count >=2 and pss.count(first_let) + pss.count(second_let) == 0:
        msg = "Password meets all conditions and Password accepted."
        return True, msg
                    # I also changed this section to meet the password criteria and added the section to test that neither of the first
                    # two letters are used 
    else:
        msg= ""
        if lng < 12:
            msg += "Password has to be at least 12 characters long \n"
        if lc_count < 2:
            msg += "Password has to have at least 2 lower case characters. \n"
        if uc_count != 2:
            msg += "Password has to have 2 upper case characters. \n"
        if dig_count != 2:
            msg += "Password has to have 2 digits. \n"
        if sp_count != 0:
            msg += "Password should not have any spaces. \n"
        if sp_ch_count < 2:
            msg += "Password should have at least 2 special characters. \n"
        if pss.count(first_let) + pss.count(second_let) > 0:
            msg += "Password should not contain the first or second letter of your first name. \n"
        return False, msg
                    # Here for any reason a certain criteria isn't met, said reason is displayed by setting and saving the reason in msg


if __name__ == "__main__":
    main()

        
