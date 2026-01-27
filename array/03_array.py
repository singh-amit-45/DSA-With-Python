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
