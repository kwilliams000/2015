def movement(direction,inputList):
    if direction == ">":
        # then add take latest value and add 0,1 
        # as a new element of the list
        0
    return 0

def addElementToList(theList,theElement):
        # take the list, get the latest element and add 
        # add the value from theElement as a new entry
        return 0

def lastListElement(listForLastElement):
        return len(listForLastElement - 1)

def splitMeasurements(strInput,splitter):
    x1 = list(strInput.split(splitter))
    x2 = list(map(int,x1))
    return x2

x = ['0,0']
z = ['1x1x10']

print(splitMeasurements(x[0],','))
print(splitMeasurements(z[0],'x'))