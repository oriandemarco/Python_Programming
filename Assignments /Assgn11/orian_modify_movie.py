# File: orian_modify_movie.py 
# Project: CSIS2101 Assignment 10
# Author: Orian Demarco 
# History: Version 1.2
# Date: November 21, 2023
# Program: Modify a Movie Record.
# Grade: 83
# Grade Comment: For append the movie does not check whether the movie is 
# already there in the file or not. The modify movie errors in compiling as 
# the amount is not obtained properly. (-17)


import os
import orian_proc_movie

def modify_movie_list(movie_file, movie_name):
    movie_file = "orian_movies.txt"
    temp_filename = "tmp_movie.txt"
    found = False
    with open ("orian_movies.txt", "r") as file, open(temp_filename, "w") as temp_file:
                    # i open the movie file in read mode and the temp file in write mode 
        line = file.readline()
        while line:
            if movie_name in line:
                split_movie = line.split(" ", 1)
                original_price = float(split_movie[1].replace("$",""))
                new_movie_price = original_price * 1.15
                temp_file.write(f"{split_movie[0]} {new_movie_price:.2f}$\n")
                found = True
                    # each line is read with the while loop and if the current line contains the movie to be 
                    # changed. the line is split into the movie and its price, then the dollar sign is esssentially removed, 
                    # and then covnerts the price into a float so i can multiply to increase the price by 15%. I then 
                    # formatted the new line (including movie and updated price) to match the original movie text file. 
                    # also set found to true to incidate the movie was found and modified 
            else:
                temp_file.write(line)
            line = file.readline()  
                    # if the movie to be changed couldn't be found in the current line being read, 
                    # the line is written into the temp file just as is. 
        if not found:
            print("Could not find that movie.")
            return False
                    # this code considers if the movie couldnt be found in the orginal 
                    # file and lets the user know in a print statement
    os.remove(movie_file)
    os.rename(temp_filename, movie_file)
                    # once the file has been modified the orignal one (orian movies text) 
                    # is deleted and then the name on the temp file is changed to the name 
                    # of the original movie text, essentially the temp replaces the original 
    return True 


def main():
    movie_name = input("Enter the name of the movie you'd like to modify: ")
    if modify_movie_list("orian_movies.txt", movie_name):
        updated_total_price = orian_proc_movie.orian_calc_stream_charges("orian_movies.txt")
        print(f"The total price of all movies is ${updated_total_price:.2f}") 
                    # i used an if statement so that its considered if the function is
                    # true or false before giving the price 

if __name__ == "__main__":
   main()
