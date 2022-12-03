calorieCount = 0
calList = []

with open("input.txt", "r") as file:
    for line in file:
        read = line.strip()
        if read.isdigit():
            calorieCount = calorieCount + int(read)
        else:
            if len(calList) == 3:
                if calorieCount > min(calList):
                    calList.append(calorieCount)
                    calList.remove(min(calList))
            else:
                calList.append(calorieCount)
            calorieCount = 0
print(sum(calList))