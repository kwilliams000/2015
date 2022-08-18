def surfaceArea(l,w,h):
    a = (l*w)
    b = (w*h)
    c = (h*l)
    """print(a)
    print(b)
    print(c)
    print(min(a,b,c))"""
    return 2*a + 2*b + 2*c + min(a,b,c)

def ribbonAmt(l,w,h):
    return (l+w+h-max(l,w,h))*2

def ribbonBowAmt(l,w,h):
    return l*w*h

def splitMeasurements(strInput):
    x = list(strInput.split("x"))
    x2 = list(map(int,x))
    return x2

def CalcTotalPaper():
    importFile = open("Day2-input.txt","r")
    data = importFile.read()

    packages = data.split("\n")

    #print(surfaceArea(1,1,1))
    #print(packages)
    total = 0
    currentLine = []
    for i in range(0, len(packages)-1):
        #print(i)
        #print(splitMeasurements(packages[i]))
        currentLine = splitMeasurements(packages[i])
        total+=surfaceArea(currentLine[0],currentLine[1],currentLine[2])

    print(total)
    importFile.close()

def CalcTotalRibbon():
    importFile = open("Day2-input.txt","r")
    data = importFile.read()

    packages = data.split("\n")

    #print(surfaceArea(1,1,1))
    #print(packages)
    total = 0
    currentLine = []
    for i in range(0, len(packages)-1):
        #print(i)
        #print(splitMeasurements(packages[i]))
        currentLine = splitMeasurements(packages[i])
        total+=ribbonAmt(currentLine[0],currentLine[1],currentLine[2])
        total+=ribbonBowAmt(currentLine[0],currentLine[1],currentLine[2])

    print(total)
    importFile.close()
"""
z = ['1x1x10']
y= splitMeasurements(z[0])

print(y)
print(surfaceArea(y[0],y[1],y[2]))"""
#CalcTotalPaper()
"""r1 = ['2x3x4']
r = splitMeasurements(r1[0])
print(ribbonAmt(r[0],r[1],r[2]))
print(ribbonBowAmt(r[0],r[1],r[2]))"""
CalcTotalRibbon()