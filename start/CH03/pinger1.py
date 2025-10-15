#!/usr/bin/env python3
# First example of pinging from Python
# By Melinda 10/6

#Import things
import os
import platform

def ping_address (ip_address):
    #Find current OS
    current_os =platform.system().lower()
    #Build ping command
    #If Windows
    if current_os == "windows" :
        ping_cmd = "ping -n 1 -w 2 ip_address >nul"
    else:
        ping_cmd = "ping -c -w 2" + ip_address + ">/dev/nul 2>&1"

    #Execute ping command
    exit_code= os.system ( ping_cmd)    
    return exit_code

#Assign Ip to variable 
ip_prefix = "192.168.0."

# start loop
for final_octet in range (254):
    #Buiild IP address
    ip_addr = ip_prefix + str( final_octet+1)
    
    #call function
    exit_code = ping_address (ip_addr)

    #Find current OS
    current_os =platform.system().lower()
    #Build ping command
    #If Windows
    if current_os == "windows" :
        ping_cmd = "ping -n 1 -w 2 ip_addr >nul"
    else:
        ping_cmd = "ping -c -w 2" + ip_addr + ">/dev/nul 2>&1"

#Execute ping command
exit_code= os.system ( ping_cmd)
#print results
print (exit_code)
if exit_code == 0:
    print (f"{ip_addr} is online")
else:
    print (f"{ip_addr} is NOT online")
