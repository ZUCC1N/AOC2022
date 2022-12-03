class house():
    def __init__(self, xCoord, yCoord):
        self._xLocation = xCoord
        self._yLocation = yCoord
        self._presentCount = 0

    def getXLocation(self):
        return self._xLocation
    
    def getYLocation(self):
        return self._yLocation

    def getPresentCount(self):
        return self._presentCount

    def addPresent(self):
        self._presentCount += 1

def doInsturctions(start, instructions, list):
    xLoc = 0
    yLoc = 0
    for j in range(start, len(instructions), 2):
        found = False
        match instructions[j]:
            case "^":
                yLoc += 1
            case ">":
                xLoc += 1
            case "v":
                yLoc -= 1
            case "<":
                xLoc -= 1

        while found == False or found != None:
            for i in range(0, len(houselist)):
                if list[i].getXLocation() == xLoc and list[i].getYLocation() == yLoc:
                    found = True
                    foundLoc = i
            break

        if found == True:     
            list[foundLoc].addPresent()
        else:
            list.append(house(xLoc, yLoc))
            list[len(houselist) - 1].addPresent()

houselist = [house(0, 0)]
houselist[0].addPresent()

instructions = open("2015/day 3/input.txt", "r").readline().strip()

doInsturctions(0, instructions, houselist)
doInsturctions(1, instructions, houselist)

print(len(houselist))