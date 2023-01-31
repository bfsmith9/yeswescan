#! /usr/bin/python3

"""
Installing Python on Windows (choose Python 3 - more modern)

https://learn.microsoft.com/en-us/windows/python/beginners

https://www.python.org/downloads/windows/

## Sample input file
9780671656607
9780449222713
42
9780449222719

## Sample output file
### Pretend header: a,b,isbn,qty,c,d,e,f
 
a,b,isbn,qty,c,d,e,f
,,9780671656607,,123456,222,6.60,
,,9780671656607,1,123456,222,6.60,
,,9780449222713,37,123456,222,5.99,
,,9780459222714,314,123456,222,5.99,

- Quantity is always 1-3 characters, no more
- Barcode is always longer
- If there's no quantity, put a "1"

## Algorithm 
- import input file
- output a header to the output file 
- Read a line
- If line > 3, save to isbn variable
- If next line <= 3, it's a quantity. Save it to found_qty variable., and output the isbn and the found_qty to the output file in the expected .csv format
- Else, output the isbn variable and the default_qty variable (1) to the output file in the expected .csv file

"""

import os
import sys
# import csv
# inputfile = "scinput.txt"
outputfile = "scoutput.txt"

inputfile = open("scinput.txt")

# Read the input file
lines = inputfile.readlines()
#csvfile = open (inputfile, 'w')

for line in lines:
    if len(line) > 3:
        print(line, end = "")
        print("---")
    else:
        print("this one is shorter")
        print(line, end = "") 
        # print(line, end = "")
        print("---")

# The lines variable holds the lines from the input file

sys.exit() 

# Read the input file
csvfile = open (inputfile, 'r')

# The lines variable holds the lines from the input file
# lines = inputfile.readlines()
reader = csv.DictReader(csvfile)

for row in reader:
	print(row['isbn'], row['qty'])


"""
Preliminary code below here 
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
        
        
---
reader = csv.DictReader(csvfile)

for row in reader:
	print(row['isbn'], row['qty'])
        
        
""" 
