#input from user in array

from array import *
arr = array('i', [])
n = int(input("Enter the number"))
for i in range(0, n):
    arr.append(int(input("Enter the inupt value")))
    for x in arr:
        print(x,end=" ") 