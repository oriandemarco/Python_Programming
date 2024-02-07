# File: orian_append_movie.py 
# Project: CSIS2101 Assignment 10
# Author: Orian Demarco 
# History: Version 1.2 
# Date: November 21, 2023
# Program: Append a Movie Record.

import orian_proc_movie

def append_new_movie(movie_file, movie, price):
    with open (movie_file, "a") as file:
        file.write (f"{movie} {price}$ \n")
            # this function takes three parameters, the actual text file along with 
            # the movies and prices in it. it then writes the new values into the text 
            # file with formatting to match the other movies in the file 

def main():
    new_movie_name = input ("Enter the name of your favorite movie: ")
    new_movie_price = input ("Enter the movie's price: ")
    append_new_movie("orian_movies.txt", new_movie_name, new_movie_price)
    total_price = orian_proc_movie.orian_calc_stream_charges("orian_movies.txt")
    print(f"The new total price for all movies is: ${total_price:.2f}")
            # i ask the user for their two inputs then call the append function. 
            # the total price is then calculated by calling the calc stream function in
            # the orian proc file taking the actual text file in as an argument

if __name__ == "__main__":
    main()