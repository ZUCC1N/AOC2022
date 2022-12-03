Move = ['X', 'Y', 'Z'] 
oppMove = ['A', 'B', 'C']

def mapGame1(rps):
    oppPick = oppMove.index(rps[0])
    pick = Move.index(rps[1])
    offset = (pick - oppPick + 1) % 3
    return(offset * 3 + pick + 1)

def mapGame2(rps):
    oppPick = oppMove.index(rps[0])
    result = Move.index(rps[1])
    offset = [2, 0, 1][result]
    pick = (offset + oppPick) % 3
    return (result * 3 + pick + 1)

with open("input.txt", "r") as file:
        rpsData = [line.strip().split(" ") for line in file]
print(sum(list(map(mapGame1, rpsData))))
print(sum(list(map(mapGame2, rpsData))))