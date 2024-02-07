# File:    Assgn9demarco.py 
# Project: CSIS2101 Assignment 9
# Author:  Orian Demarco 
# History: Version 1.1 November 5, 2023
# Program: Strings.
# Grade: 75/100
# Grade Comment: Function one is not done as per specs. You need to iterate over the string. 
# (-20) Functions 2 works. But using if 'A' <= char <= 'C': converted_num += '2' is not a 
# good idea. (-5) Function 3 is good


def oO_replace(original_string, old_substring, new_substring):
    if original_string.count(old_substring) < 2:
        return original_string
                # First, I checked to see if the old string occurs more than once in the 
                # user's original inputted string by using .count. If there aren't 2 
                # occurances of a specified old string, the original string is 
                # returned to the replace function. 

    first_occur = original_string.find(old_substring)
    second_occur = original_string.find(old_substring, first_occur + 1)
                # If there are two occurances of old_substring in original_string, I use find
                # to find the index of the first occurance of old_substring and store this index 
                # value inside the vairable first_occur.
                # I use find again to search for the second occurance of the 
                # orginal string by starting in the position right after where the first 
                # occurance was found. Once it's found, the index is stored in seccond_occur
                # For example if original string is mississippi and oldsubstring is iss
                # firs_occur value would be 1 (where first iss starts) and second_occur 
                # value would be 4 (where second iss starts)

    before_sec_occur = original_string[:second_occur]
    after_sec_occur = original_string[second_occur + len(old_substring):]

    new_string = before_sec_occur + new_substring + after_sec_occur
    print ("New String:",new_string)  
                # In this section, I split the original string into 3 parts based on the old 
                # substring relevant to the placement of the seccond occurance. So for example, 
                # if I used the word Mississippi, there are three parts: before the seccond occurance
                # of the oldsubstring(miss) the oldsubstring itself (iss) and after the second occurance 
                # (ippi) On line 28 I then simply replace the oldsubstring (iss) with (izz) 

def oONumberConverter(original_phone_num):
    converted_phone_num = ""
    
    for char in original_phone_num:
        if char.isalpha():
            char = char.upper()
            if 'A' <= char <= 'C':
                converted_phone_num += '2'
            elif 'D' <= char <= 'F':
                converted_phone_num += '3'
            elif 'G' <= char <= 'I':
                converted_phone_num += '4'
            elif 'J' <= char <= 'L':
                converted_phone_num += '5'
            elif 'M' <= char <= 'O':
                converted_phone_num += '6'
            elif 'P' <= char <= 'S':
                converted_phone_num += '7'
            elif 'T' <= char <= 'V':
                converted_phone_num += '8'
            elif 'W' <= char <= 'Z':
                converted_phone_num += '9'
        else: 
            converted_phone_num += char

    return converted_phone_num
                # First I initialize an empty string to store the converted phone number. 
                # I then used a for loop so I can iterate over each character within the 
                # user's inputed phone number. If a given inputed character is an alphabetic character 
                # it's then converted to uppercase to make sure there's no issues with case sensitivity. 
                # Then it's run through a series of if statements to find the numberic value corresponding to 
                # the given character. If a given input character isn't alphebetic (like a hyphen) it's 
                # simply appended to the converted number as is.

def oO_Pig_Latin(UpperCase):
    words = UpperCase.split()
    pig_lat_words = []

    for word in words:
        word = word.upper()
        if len(word) >= 2:
            first_char = word[0]
            last_char = word [-1]
            pig_lat_word = last_char + word[1:-1] + first_char + "2101"
            pig_lat_words.append(pig_lat_word)
        else:
            pig_lat_words.append(word + "2101")

    return " ".join(pig_lat_words)
                # I first take the user's original sentence (UpperCase) as an argument in the Pig Latin function
                # I then split the sentence into individual words and store the words in the 'words' list. 
                # I also initialize an empty list to store the pig latin version of the words.
                # The function goes through a loop to analyze each word in my 'words' list. It first turn all words 
                # into uppercase then checks if the word has at least 2 characters. If the word does, 
                # the first character and last charcter of a given word are stored in variables. The pig latin 
                # version of the word is then created by the pig_lat_word by moving the first character to the end,
                # adding 2102 to the end, and placing the last character in the begining. Each pig latin word is then 
                # appended to the pig latin words list I initialized on line 72. If the word only has one character 
                # (like "I") then simply 2101 is appended to the latin word list after the given character. 
                # After processing each word from the orginal sentence into pig latin, 
                # the new words are joined together and returned to the orginal function. 

def main ():
    original_string = input("Please enter the orginal string: ")
    old_substring = input("Please enter the old substring: ")
    new_substring = input("Please enter the new substring: ")
    oO_replace(original_string, old_substring, new_substring)
    print(" ")
                # Inputs and calling the oO_replace function in the main


    original_phone_num = input("Please enter a 10 character phone number: ")
    converted_phone_num = oONumberConverter(original_phone_num)
    print ("Converted phone number:", converted_phone_num)
    print(" ")
                # Inputs, calling the oO_NumberConverter function in the main, 
                # and printing results 


    UpperCase = input("Please enter a sentence: ")
    pig_latin_sentence = oO_Pig_Latin(UpperCase)
    print ("Pig Latin Sentence:", pig_latin_sentence)
    print(" ")

                # Inputs, calling the oO_Pig_Latin function in the main, converting 
                # the joined pig latin words into an actual sentence variable and 
                # printing results 

main()

