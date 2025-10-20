#!/usr/bin/env python3
# Sample script that writes to a file
# By 
#10/15

import os
# get current directory
script_path = os.path.abspath (__file__)
script_dir = os.path.dirname (script_path)
# build file path
file_path = os.path.join (script_dir, "testfile.txt")


# create file object
f = open( file_path, "w")

#write to file object
f.write ("My name is Ed\n ")
f.write(" I like rubber ducks ")
f.write (" Hello World\n ")

#close file object
f.close()