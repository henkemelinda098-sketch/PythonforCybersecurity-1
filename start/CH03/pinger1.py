#!/usr/bin/env python3
# First example of pinging from Python
# By Melinda 10/6

#Import things
import os

#Assign Ip to variable 
ip_addr = "127.0.0.1"

#Build ping command
ping_cm = "ping -c 1 -W 2  " + ip_addr + " > /dev/null 2>&1"
print (ping_cmd)
#Execute ping command
exit_code= os.system ( ping_cm)
#print results
print (exit_code)
if exit_code == 0:
    print (f"{ip_addr} is online")
else:
    print (f"{ip_addr} is NOT online")
