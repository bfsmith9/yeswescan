#! /usr/bin/python3

"""
yeswecan! 
Barry Smith February 2023 

## Installing Python on Windows (choose Python 3 - more modern)

<https://www.python.org/downloads/windows/>

## Sample input file  
9780671656607  
9780449222713  
42  
9780449222719  

## Header

Unused Field, Sequence, Barcode, Quantity, Dept/Cat, User, Price, Area,  

## Sample output file

Unused Field, Sequence, Barcode, Quantity, Dept/Cat, User, Price, Area,  
,,9780671656607,,123456,222,6.60,  
,,9780671656607,1,123456,222,6.60,  
,,9780449222713,37,123456,222,5.99,  
,,9780459222714,314,123456,222,5.99,  

- Quantity is always 1-3 characters, no more
- Barcode is always 4 characters or longer
- If there's no quantity, put a "1" as the default quantity

## Algorithm 
- Start GUI input boxes to get user, dept 
- import input file
    - Read it once to get the last line; close
    - Open again to read each line 
- Open output file
- Output a header to the output file 
- Read a line
- If line > 3, save to isbn variable
- If next line <= 3, it's a quantity. Save it to found_qty variable, and output the isbn and the found_qty to the output file in the expected .csv format
- Else, output the isbn variable and the default_qty variable (1) to the output file in the expected .csv file

## NOTES
- Python's (len) can include the newline character

2/1/2023
- Customer wants Dept/Cat & User as well, which are the fields directly after QTY, respectively. After that there are two more fields we won't fill in, "Price" & "Area", so just two more commas added to the end.

"""

import os
import sys
import glob 
import tkinter as tk
from tkinter import simpledialog
# import csv


# Default dept, user 
dept = "default_dept"
user = "jane_doe"

# GUI section
ROOT = tk.Tk()
ROOT.withdraw()

# input dialog - get user name
user = simpledialog.askstring(title="User",
                                  prompt="What's your Name?:")

# check it out
# print("Hello", user)

# input dialog - get dept name
dept = simpledialog.askstring(title="Dept",
                                  prompt="What's your Dept?:")
  
# check it out
# print("Hello", dept)   

# End GUI section 

# Find the input file. It has to be in *one directory/folder* 
# below the current one, and has to have a .txt suffix 

# Array that holds the input file
inputfilearray = glob.glob('*/*.txt', recursive=True)

# Grab the input file from the array it's in
theInputFile = inputfilearray[0]

# More setup variables 
header = "Unused Field, Sequence, Barcode, Quantity, Dept/Cat, User, Price, Area,"
isbnholder = "initial"
isbnholder_nextline = "initial"
default_qty = "1"
isbnflag = 0
qtyflag = 0
last_line_flag = 0
last_line_count = 0
process_count = 0

# Read the last line of input file. If it's an ISBN, 
# we need to give it a qty, because we're always reading
# one below ISBNs to find any potential quantities there.
# Of course, that qty will be 1. 
with open(str(theInputFile)) as f:
    for line in f:
        last_line_count = last_line_count + 1
        pass
    last_line = line
    the_last_line_number = last_line_count

if len(last_line) > 4:
    last_line_flag = 1

f.close()

# Open both the input file (again) and the output file 
inputHandle = open(theInputFile)
outputHandle = open("scoutput.txt", 'w')

# Write the header to the output file
outputHandle.write(header + "\n") 
# Read the input file. 
# The lines variable holds the lines from the input file
lines = inputHandle.readlines()
#csvfile = open (inputHandle, 'w')

for line in lines:
    process_count = process_count + 1
	
    if len(line) > 4 and isbnflag == 0:
        qtyflag = 0
        isbnflag = isbnflag + 1
        isbnholder = line.rstrip()
        # print(line, end = "")
        # print("---")
        continue
        
    if len(line) > 4 and isbnflag > 0:
        if qtyflag == 1:
            isbnholder = line.strip()
            qtyflag = 0
        isbnflag = isbnflag + 1
        isbnholder2 = line.rstrip()
        # print(line, end = "")
        # print("---")
        outputHandle.write(",," + isbnholder + "," + default_qty 
        +  "," + dept + "," + user + ",,\n")
        isbnholder = isbnholder2
        # outputHandle.write(isbnholder2 + "," + default_qty)
                
    if len(line) <= 4:
        # print("this one is shorter")
        isbnflag = 0
        qty = line
        qtyflag = 1
        # print(line, end = "") 
        outputHandle.write(",," + isbnholder.rstrip() + "," + qty.rstrip() 
        +  "," + dept + "," + user + ",,\n")

        # print(line, end = "")
        # print("---")

    if len(line) > 4 and last_line_flag > 0 and process_count == last_line_count:
        outputHandle.write(",," + line + "," + default_qty 
        +  "," + dept + "," + user + ",,\n")

inputHandle.close()
outputHandle.close()

# Exit program 
# sys.exit() 

"""
# Old CSV code we're not using 
csvfile = open (inputHandle, 'r')

# lines = inputHandle.readlines()
reader = csv.DictReader(csvfile)

for row in reader:
	print(row['isbn'], row['qty'])

-----------------------
Other old code.......................
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
