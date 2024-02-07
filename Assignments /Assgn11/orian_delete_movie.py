# File: orian_delete_movie.py 
# Project: CSIS2101 Assignment 10
# Author: Orian Demarco 
# History: Version 1.2
# Date: November 21, 2023
# Program: Delete a Movie Record.

import os
import orian_proc_movie

def delete_movie_list(movie_file, movie_name):
    temp_filename = "tmp_movie.txt"
    with open (movie_file, "r") as file, open(temp_filename, "w") as temp_file:
        found = False
        line = file.readline()
        while line:
            if movie_name in line:
                found = True
            else:
                temp_file.write(line)
            line = file.readline()
                    # the orginal movie file is open to be read from and the temp file is written in. 
                    # each line is read and if the given line doesnt contain the movie name inputed 
                    # by the user to be deleted, the line is simply written into the temp file as is.
                    # if the line being looked for is found it's not written into the temp file, 
                    # meaning its deleted. 
        if not found:
            print("Could not find that movie. ")
            return False
                    # if the movie couldn't be found after reading each line a print statement is given to 
                    # let the user know and returns false
    os.remove(movie_file)
    os.rename(temp_filename, movie_file)
    return True 
                    # once the movie has been deleted the orignal one (orian movies text) 
                    # is deleted and then the name on the temp file is changed to the name 
                    # of the original movie text, essectially the temp replaces the original 

def main():
    movie_name = input("Enter the name of the movie you'd like to delete: ")
    if delete_movie_list("orian_movies.txt", movie_name):
        updated_total_price = orian_proc_movie.orian_calc_stream_charges("orian_movies.txt")
        print(f"The new total price of all movies after deleting the movie is ${updated_total_price:.2f}")
                    # i used an if statement so that its considered if the function is
                    # true or false before giving the price

if __name__ == "__main__":
    main()