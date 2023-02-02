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

## NOTES
- Python's (len) can include the newline character
- Working so far, but have to add a 1 on the end if the last 
string isn't a qty (if it's an ISBN). 
    - OK - fixed

2/1/2023
- They want Dept/Cat & User as well, which are the fields directly after QTY, respectively. After that there are two more fields we won't fill in, "Price" & "Area", so just two more commas added to the end.

"""

import os
import sys


import tkinter as tk
from tkinter import simpledialog

dept = "default_dept"
user = "jane_doe"

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
user = simpledialog.askstring(title="User",
                                  prompt="What's your Name?:")

# check it out
print("Hello", user)

dept = simpledialog.askstring(title="Dept",
                                  prompt="What's your Dept?:")
                                  
   
# check it out
print("Hello", dept)   


# import csv
# inputfile = "scinput.txt"

isbnholder = "initial"
isbnholder_nextline = "initial"
default_qty = "1"
isbnflag = 0
qtyflag = 0
last_line_flag = 0
last_line_count = 0
process_count = 0



# Read the last line of input file
with open("scinput.txt") as f:
    for line in f:
        last_line_count = last_line_count + 1
        pass
    last_line = line
    the_last_line_number = last_line_count

if len(last_line) > 4:
    last_line_flag = 1

f.close()


inputfile = open("scinput.txt")
outputfile = open("scoutput.txt", 'w')

# Read the input file
lines = inputfile.readlines()
#csvfile = open (inputfile, 'w')

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
        outputfile.write(",," + isbnholder + "," + default_qty 
        +  "," + dept + "," + user + ",,\n")
        isbnholder = isbnholder2
        # outputfile.write(isbnholder2 + "," + default_qty)
                
    if len(line) <= 4:
        # print("this one is shorter")
        isbnflag = 0
        qty = line
        qtyflag = 1
        # print(line, end = "") 
        outputfile.write(",," + isbnholder.rstrip() + "," + qty.rstrip() 
        +  "," + dept + "," + user + ",,\n")

        # print(line, end = "")
        print("---")

    if len(line) > 4 and last_line_flag > 0 and process_count == last_line_count:
        outputfile.write(",," + line + "," + default_qty 
        +  "," + dept + "," + user + ",,\n")

# The lines variable holds the lines from the input file

inputfile.close()
outputfile.close()
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
