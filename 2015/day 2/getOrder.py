paperCount = 0
ribbonCount = 0

with open("input.txt", "r") as file:
    for line in file:
        read = list(map(int, line.strip().split("x")))
        paperCount += 2*(read[0]*read[1] + read[1]*read[2] + read[2]*read[0])+ min(read[0]*read[1], read[1]*read[2], read[2]*read[0])
        ribbonCount += read[0]*read[1]*read[2] + 2*min(read[0] + read[1], read[1] + read[2], read[2] + read[0])

print(paperCount)
print(ribbonCount)