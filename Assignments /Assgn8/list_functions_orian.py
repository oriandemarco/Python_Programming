# File:    Assgn9demarco.py 
# Project: CSIS2101 Assignment 9
# Author:  Orian Demarco 
# History: Version 1.1 November 5, 2023
# Program: Strings.

def range_avg_of_list_orian(number_list):
    if not number_list:
        return None
            # I put this to handle an empty list 
    return (max(number_list) + min(number_list)) / 2
            # This function returns the average of the 
            # maximum and minimum value of the list.
    
def avg_of_list_orian(number_list):
    if not number_list:
        return None
    return sum(number_list) / len(number_list)
            # Once again, I used 'if not return none' to handle
            # a potentially empty list, I also found the average in 
            # this function by summing up all list numbers and dividing 
            # that by the amount of items on the list

def haircut_list_orian(number_list, clip_num):
    clipped_list = []
    for num in number_list:
        if num > clip_num:
            clipped_list.append(clip_num)
        else:
            clipped_list.append(num)
    return clipped_list
            # In this function, I first created the clipped list then 
            # the inputed clip number (clip_num) is compared with each item on 
            # the original list then the specified clip num replaces 
            # any given number within the list thats greater than clip_num
            # the use of append adds these values to the new list and finally
            # the new list is returned to the haircut function 
   
def mode_of_list_orian(number_list, item):
    return number_list.count(item)
            # This function returns the count of a given item in the list
            # (number_list) based on the users integer input 'item'
    
def median_of_list_orian(number_list_copy):
    if not number_list_copy:
        return None
    number_list_copy.sort()
    list_length = len(number_list_copy)
    middle = list_length // 2
    
    if list_length % 2 == 0:
        list_median = (number_list_copy[middle - 1] + number_list_copy[middle]) / 2
    else:
        list_median = number_list_copy[middle]       

    return list_median 
            # First, a copy of the list (number_list_copy) is passed as an argument.
            # Again, 'if not return none' is then used to consider a list where n=0. 
            # I then sort this copied list and get its length. I then defined 'middle' 
            # as the length of the list divided by two using the floor operator, which
            # will divide list_length by 2 and round the result down to the nearest whole 
            # number. # I then consider if the list has an even number of elements, 
            # then calculate the average of the two middle items. The -1 is becuase the
            # first element in an index is 0. If the list is odd the middle value of the 
            # list will be returned without the need to find an average first. 

def main_list():
    number_list = []
    n = int(input("Enter the number of items to add to the list: "))
            # Creates an empty list and asks the user for the number of items to be added

    for i in range(n):
        num = int(input("Enter a number: "))
        number_list.append(num)
            # Asks the user for each number in the list to be added, and append adds 
            # them to the list

    print("Given List:", number_list)
    print("Range Average of the List is:", range_avg_of_list_orian(number_list))
    print("Average of the List is:", avg_of_list_orian(number_list))

    number_list_copy = []
    for i in number_list:
        number_list_copy.append(i)
    print("Median of the List is:", median_of_list_orian(number_list_copy))
            # I return the users list, range list average, actual list average, and then the 
            # median by using a copy of number_list as an argument. The copy was made by creating
            # a new list and appending each element from the orginal copy to the new one.
            
    item = int(input("Enter an item to find its mode: "))
    print(f"Mode of {item} in the List is:", mode_of_list_orian(number_list, item))
            # I ask the user to input a specific item to find the mode then return the result 
            # in an f statement so I can also specify their original choice as well as the 
            # functions returned value based on the given arguments 

    clip_num = int(input("Enter a value to clip the list: "))
    print(f"List after clipping with {clip_num} is:", haircut_list_orian(number_list, clip_num))
            # I ask the user to input a specific number to use as a clip value then specify that 
            # the new list (clipped_list) is equal to the the haircut function with its given 
            # arguments. Then I return the result in an f statement so I can also specify their
            # original clip value.

main_list()
            # I call the main function 
