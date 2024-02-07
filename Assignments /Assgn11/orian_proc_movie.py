# File: orian_proc_movie.py 
# Project: CSIS2101 Assignment 11
# Author: Orian Demarco 
# History: Version 1.2
# Date: November 21, 2023
# Program: File Processing.

def orian_calc_stream_charges(movie_file):
    total_movie_price = 0
    with open(movie_file, "r") as file:
        line = file.readline()
        while line:
            price = float(line.split("$")[0].split()[-1])
                # This splits each line by the dollar sign. Then splits each word by the space. Like for example 
                # "Top Gun: Maverick 9.99$" gets split by ["Top Gun: Maverick 9.99", "$"] then into 
                # ["Top", "Gun:", "Maverick", "9.99"] then the [-1] selected the last element 9.99 and turns it into a float
            total_movie_price += price
            line = file.readline()
    return total_movie_price
                # the value of all prices is added to total_movie_price then gets returned to the orginal function 

def main():
    total_movie_price = orian_calc_stream_charges("orian_movies.txt")
    print (f"The total price of watching all movies is ${total_movie_price:.2f}")
                # i set total_movie_price = to the calc stream function with the text file as an argument. 

if __name__ == "__main__":
    main()