#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Melinda Henke 10/20


# Get message from user
message = input("What is the message: ")
message = message.upper ()
final_message = ""

#For each letter in message
for letter in message:
    #Convert letter in message
    converted_letter =ord (letter)
   
    #Check for letter
    if converted_letter >= 65 and converted_letter <= 90:
        #Add 13 to number
        converted_letter += 13
        #Past Z?
        if converted_letter > 90: 
            #Substract 26 from number
            converted_letter -= 26
        #Convert number to letter
        upt_letter = chr (converted_letter)
        final_message += upt_letter
    else: 
        final_message += letter

#Print updated message
print (final_message)
