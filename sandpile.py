#imports
import random
import time

def toString(arr:list[int]) -> str:
    length = int(len(arr) ** 0.5)
    out = ''
    for row in range(length):
        for col in range(length):
            out += f'[{arr[row*length+col]}] '
        if row < length-1:
            out += '\n'
    return out

#get value
def get(arr:list[int], index:int) -> int:
    return arr[int]

#get index (left, right, up, down)
def getLeft(arr:list[int], index:int) -> int:
    sideLength = int(len(arr) ** 0.5)
    if index % sideLength == 0:
        return None
    #return arr[index-1]
    return index - 1
def getRight(arr:list[int], index:int) -> int:
    sideLength = int(len(arr) ** 0.5)
    if (index+1) % sideLength == 0:
        return None
    #return arr[index+1]
    return index + 1
def getUp(arr:list[int], index:int) -> int:
    sideLength = int(len(arr) ** 0.5)
    if index // sideLength == 0:
        return None
    #return arr[index-sideLength]
    return index - sideLength
def getDown(arr:list[int], index:int) -> int:
    sideLength = int(len(arr) ** 0.5)
    if index // sideLength == sideLength-1:
        return None
    #return arr[index+sideLength]
    return index + sideLength
def getValidCardinal(arr:list[int], index:int) -> list[int]: #arr is full array
    cardinalIndex = [getLeft(arr, index), getRight(arr, index), getUp(arr, index), getDown(arr, index)]
    while None in cardinalIndex:
        cardinalIndex.remove(None)
    return cardinalIndex

#q methods: Q TURNED INTO A STACK
def enq(arr:list[int], element:int) -> list[int]: #maybe return nothing
    #arr.insert(0, element)
    arr.append(element)
    return arr
def deq(arr:list[int]) -> int:
    return arr.pop()
def showq(arr:list[int]) -> str:
    out = '['
    for i in range(len(arr)):
        out += f'{arr[i]}'
        if i != len(arr)-1:
            out += f', '
    out += ']'
    return out

def recursiveCollapse(arr:list[int], q:list[int], limit:int, iter:int) -> list[int]: #big collapse function
    if len(q) == 0: #exit condition
        return arr
    index = deq(q)
    print(f'iter: {iter}')
    print(toString(arr)) #display
    #collapse function
    cardinalIndex = getValidCardinal(arr, index)
    while arr[index] >= limit:
        arr[index] -= limit
        for i in cardinalIndex:
            arr[i] += 1
            if arr[i] >= limit:
                if i not in q:
                    enq(q, i)
    print(f'q:{showq(q)}\n')
    time.sleep(1.5)#wait time
    return recursiveCollapse(arr, q, limit, iter+1) #recursive call

#define a check stabilization function, searches through the array for any int > limit, if so adds it to q and calls recCollapse
def checkStable(arr:list[int], q:list[int], limit:int) -> list[int]:
    stable = True
    for i in range(len(arr)):
        if arr[i] >= limit:
            stable = False
            enq(q, i)
            break
    return stable

#creating array of random numbers
#arr1 = [None] * 16
arr1 = [4] * 9
q = []
limit = 4
#for i in range(len(arr1)):
#    arr1[i] = random.randint(0, 8)

#testing block:
iter = 0
while not checkStable(arr1, q, limit):
    arr1 = recursiveCollapse(arr1, q, limit, iter)

print('stable output')
print(toString(arr1))

'''
#testing block
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
length = len(arr1)
print(toString(arr1))
print('getting right')
for i in range(length):
    print(getRight(arr1, i))
print('\ngetting left')
for i in range(length):
    print(getLeft(arr1, i))
print('\ngetting up')
for i in range(length):
    print(getUp(arr1, i))
print('\ngetting down')
for i in range(length):
    print(getDown(arr1, i))

#testing block
startIndex = random.randint(0, len(arr1))
q = []
enq(q, startIndex)
print(showq(q))
print(deq(q))
print(showq(q))

#testing block
print(toString(arr1))
print(f'starting index: {startIndex}')
print(f'left of start: {getLeft(arr1, startIndex)}')
print(f'right of start: {getRight(arr1, startIndex)}')
print(f'up of start: {getUp(arr1, startIndex)}')
print(f'down of start: {getDown(arr1, startIndex)}')
'''