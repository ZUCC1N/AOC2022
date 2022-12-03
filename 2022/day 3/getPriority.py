def findPriority(char): # does some fancy stuff to centralise and extract priority
    return (ord(list(char)[0])-38) % 58

def extractRucksacks(file): # just reads the file
    sacks = open(file, "r").read().strip().split("\n")
    return sacks

def findDuplicateTwo(sack): # part 1
    return set(sack[:len(sack) >> 1]) & set(sack[len(sack) >> 1:])

def findDuplicateThree(sack1, sack2, sack3): # part 2
    return set(sack1) & set(sack2) & set(sack3)

# main code 
sacks = extractRucksacks("2022/day 3/input.txt") # get the sacks

# part 1
overlap = list(map(findDuplicateTwo, sacks))
print(sum(list(map(findPriority, overlap))))

# part 2
overlap = []
for i in range(0, len(sacks),3):
    overlap.append(findDuplicateThree(sacks[i], sacks[i + 1], sacks[i + 2]))
print(sum(list(map(findPriority, overlap))))