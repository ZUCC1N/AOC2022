orientation = 0
xLoc = 0
yLoc = 0
visited = []
instuctions = open("2016/day 1/input.txt", "r").readline().strip().split(", ")
for entry in instuctions:
    match entry[0]:
        case "R":
            orientation = (orientation + 1) % 4
        case "L":
            orientation = (orientation - 1) % 4
    
    match orientation:
        case 0:
            for i in range(yLoc, int(''.join(c for c in entry if c.isdigit()))):
                visited.append([])
            yLoc += int(''.join(c for c in entry if c.isdigit()))
        case 1:
            xLoc += int(''.join(c for c in entry if c.isdigit()))
        case 2:
            yLoc -= int(''.join(c for c in entry if c.isdigit()))
        case 3:
            xLoc -= int(''.join(c for c in entry if c.isdigit()))

print(abs(xLoc) + abs(yLoc))