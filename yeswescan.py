#! /usr/bin/python3

"""
Installing Python on Windows (choose Python 3 - more modern)

https://learn.microsoft.com/en-us/windows/python/beginners

https://www.python.org/downloads/windows/

Sample Scanpal file:
 
,,978044020133550495,1,123456,222,04.95,
,,9780671656607,1,123456,222,6.60,
,,9780449222713,1,123456,222,5.99,
,,978042520581550799,1,123456,222,07.99,

Beth only wants the barcode and the quantity (the number right after the first long barcode, which is either 13 characters or...

Plan: import input file, grab barcode & quantity, output that to an output file.

"""

import os

# Read the input file
inputfile= open ("scanpal.txt", 'r')

# The lines variable holds the lines from the input file
lines = inputfile.readlines()

# Do something to each line
for line in lines:
    if len(line) == 14:
        print(line, end = "")
        print("---")
    else:
        print("this one is longer")
        print(line, end = "") 
        print(line[14:], end = "")
        print("---")
