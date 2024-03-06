import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import sandpile as sp

#testing block
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
length = len(arr1)

print(sp.toString(arr1)) #display array

print('getting right')
for i in range(length):
    print(sp.getRight(arr1, i)) #get all valid 'right' values
print('\ngetting left')
for i in range(length):
    print(sp.getLeft(arr1, i)) #get all valid 'left' values
print('\ngetting up')
for i in range(length):
    print(sp.getUp(arr1, i)) #get all valid 'up' values
print('\ngetting down')
for i in range(length):
    print(sp.getDown(arr1, i)) #get all valid 'down' values