#Diff between Arrays and List
#   Arrays will have elements with same data types
#   List can have elements with multiple data types
# 

from array import *

myArray = array('i', [1,2,3,4,5])
myArray.append(6)

print(myArray)

myArray.insert(0,0)
print(myArray)

myExtendedArray = array('i', [7,8,9,10])

myArray.extend(myExtendedArray)
print(myArray)

