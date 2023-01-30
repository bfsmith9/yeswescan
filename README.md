# yeswescan

## NOTES

- The quantity will only be 1-3 characters. No thousands or more
- After the output of one without any number, put a "1" for the quantity. 

## Sample input file
9780671656607
9780449222713
42
9780449222719

## Sample output file
### Header
Unused field,Sequence,Barcode,Quantity,Dept/Cat,User,Price,Area,Field
 
Unused field,Sequence,Barcode,Quantity,Dept/Cat,User,Price,Area,Field
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
- Loop, reading each line
- If line > 3, save to isbn variable
- If next line <= 3, it's a quantity. Save it to `found_qty` variable, and output the isbn and the `found_qty` to the output file in the expected .csv format
- Else, output the isbn variable and the default_qty variable (1) to the output file in the expected .csv file