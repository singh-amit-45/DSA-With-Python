import array

# Array print
val = array.array('i', [1, 2, 3, 4, 5, 6])
print(val)
print('---------------------------------------------')

# Index based iteration
for i in range(0, 6):
    print(val[i])
print('---------------------------------------------')

# Direct iteration
for x in val:
    print(x)
print('---------------------------------------------')


from array import *

# New array (short method)
val = array('i', [1, 2, 3, 4, 5])
print(val)
print('---------------------------------------------')

# Direct iteration on new array
for x in val:
    print(x)
print('---------------------------------------------')

# Typecode of array
print(val.typecode)
print('---------------------------------------------')

# Reverse array
val.reverse()
print(val)
print('---------------------------------------------')

# Index based after reverse
for i in range(0, len(val)):
    print(val[i])
print('---------------------------------------------')

#insert ,append,replace
val.insert(1, 50)
val.append(100)
val[2] = 200
for i in range (0, len(val)):
    print(val[i], end=' ')
print('---------------------------------------------')
