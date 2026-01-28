# Example of Slicing in Array
from array import *
val = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
abc = val[2:7]
for i in range(len(abc)):
    print(abc[i],end=" ")


#REVERSE SLICING IN ARRAY

from array import *
val = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
abc = val[::-1]
for i in range(len(abc)):
    print(abc[i],end=" ")


#input from user in  array

from array import *
arr = array('i', [])
n = int(input("Enter the number"))
for i in range(0, n):
    arr.append(int(input("Enter the inupt value")))
    for x in arr:
        print(x,end=" ") 