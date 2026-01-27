#copying an array using array() function
from array import *
val = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
CopyArray = array(val.typecode, (x for x in val))
for i in range(len(val)):
    print(CopyArray[i],end=" ")

