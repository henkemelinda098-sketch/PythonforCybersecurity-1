#!/usr/bin/env python3
# example workign with conditionals
#By Melinda Henke 10/10

#ask the user if today is a good day
answer = input ("Is today a good day? (y/n)")

#check the user's response 
if answer.lower() == "y":

#use a loop to print the message 10 times
    for i in range (10):
        print("Yeah it is")
