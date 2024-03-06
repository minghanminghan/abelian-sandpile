#imports
import random
import time

def toString(arr:list[int]) -> str:
    length = int(len(arr) ** 0.5)
    out = ''
    for row in range(length):
        for col in range(length):
            out += f'[{arr[row*length+col]}] '
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
    if len(arr) == 0:
        return ''
    out = 'q:['
    for i in range(len(arr)):
        out += f'{arr[i]}'
        if i != len(arr)-1:
            out += f', '
    out += ']\n'
    return out

def recursiveCollapse(arr:list[int], q:list[int], limit:int, iter:int) -> list[int]: #big collapse function
    if len(q) == 0: #exit condition
        return arr
    index = deq(q)
    print(f'iteration #{iter}')
    print(showq(q))
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
    time.sleep(0.5)#wait time
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

def main():
    #getting vars
    length = int(input('array sidelength >'))
    limit = int(input('sandpile limit >'))

    #creating vars
    pile = [None]* (length**2)
    q = []
    for i in range(len(pile)):
        pile[i] = random.randint(0, int(limit*1.5))
    iter = 0

    #running collapse function
    while not checkStable(pile, q, limit):
        pile = recursiveCollapse(pile, q, limit, iter)

    #final output
    print('stable output')
    print(toString(pile))

main()
