# yeswecan! 
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

## 2/1/2023
- Customer wants Dept/Cat & User as well, which are the fields directly after QTY, respectively. After that there are two more fields we won't fill in, "Price" & "Area", so just two more commas added to the end.
