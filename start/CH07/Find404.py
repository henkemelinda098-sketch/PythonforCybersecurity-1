#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Melinda 11/3
import os

# Ask which file to open
log_file = input ("Which file to analyze? ")

# get current directory
script_path = os.path.abspath (__file__)
script_dir = os.path.dirname (script_path)
# build file path
file_path = os.path.join (script_dir, "testfile1f.txt")

# open log file
f = open (file_path, "r")

#Read the file line by line
while True:
    line = f.readline()
    if not line:
        break
    # look for 404
    if "404" in line:
        # print line
        print(line)

# Close file
f.close()