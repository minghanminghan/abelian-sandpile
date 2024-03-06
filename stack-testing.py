#import os
#import sys
#import inspect

#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.insert(0, parentdir) 

import sandpile as sp

#testing stack function 
#(it's named as q because i thought a queue implementation would be better but using a stack gives better visuals)
q = [1,2,3,4,5] #test stack

print(sp.enq(q, 6)) #returns array
print(sp.showq(q)) #returns array
print(sp.deq(q)) #returns popped int
print(sp.showq(q))
