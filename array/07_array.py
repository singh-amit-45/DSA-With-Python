# use linspace to create an array of evenly spaced values

from numpy import *

val = linspace(0, 10, 5)
for x in val:
    print(x, end=" ")
