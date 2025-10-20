#!/usr/bin/env python3
# example workign with conditionals
#By Melinda Henke 10/10

#def function
def send_message():
    # use a loop to print the message
    for i in range (10):
        print ("Yeah it is")

#ask the user if today is a good day
answer = input ("Is today a good day? (y/n)")

#check the user's response 
if answer== "y": 
    send_message ()
