#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Melinda Henke 10/20

#create loop 0-127
for num in range (128):
    # print value and chr () output
    print (f"{num} '{chr(num)}'")