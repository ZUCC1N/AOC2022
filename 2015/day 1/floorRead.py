floor = 0
instructionPosition = 1

with open("input.txt", "r") as file:
    read = file.readline().strip()
    
for char in read:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

    if floor == -1:
        print(instructionPosition)
    
    instructionPosition += 1

print(floor)