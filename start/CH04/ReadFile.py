#!/usr/bin/env python3
# Sample script that reads from a file
# By 


import os
# get current directory
script_path = os.path.abspath (__file__)
script_dir = os.path.dirname (script_path)
# build file path
file_path = os.path.join (script_dir, "testfile1.txt")


# create file object
f = open( file_path, "r")

# read file object
print (f.read())

#close file object
f.close()