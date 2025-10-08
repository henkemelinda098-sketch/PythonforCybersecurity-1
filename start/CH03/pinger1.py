#!/usr/bin/env python3
# First example of pinging from Python
# By Melinda 10/6

#Import things
import os
import platform

#Assign Ip to variable 
ip_addr = "169.254.1.1"

#Find current OS
current_os =platform.system().lower()
#Build ping command
# #If Windows
if current_os == "windows" :
    ping_cmd = "ping -n 1 -w 2 ip_addr >nul"
else:ping_cmd = "ping -c 1 -W 2  " + ip_addr + " > /dev/null 2>&1"
    ping_cmd = "ping -n -w 2 ip_addr>nul"
else:ping_cmd = "ping -c 1 -W 2  " + ip_addr + " > /dev/null 2>&1"



    
print (ping_cmd)

#Execute ping command
exit_code= os.system ( ping_cm)
#print results
print (exit_code)
if exit_code == 0:
    print (f"{ip_addr} is online")
else:
    print (f"{ip_addr} is NOT online")

#