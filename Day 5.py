# [G]                 [D] [R]        
# [W]         [V]     [C] [T] [M]    
# [L]         [P] [Z] [Q] [F] [V]    
# [J]         [S] [D] [J] [M] [T] [V]
# [B]     [M] [H] [L] [Z] [J] [B] [S]
# [R] [C] [T] [C] [T] [R] [D] [R] [D]
# [T] [W] [Z] [T] [P] [B] [B] [H] [P]
# [D] [S] [R] [D] [G] [F] [S] [L] [Q]
#  1   2   3   4   5   6   7   8   9 

countMoves = 0

Stack1 = ["D","T","R","B","J","L","W","G"]
Stack2 = ["S","W","C"]
Stack3 = ["R","Z","T","M"]
Stack4 = ["D","T","C","H","S","P","V"]
Stack5 = ["G","P","T","L","D","Z"]
Stack6 = ["F","B","R","Z","J","Q","C","D"]
Stack7 = ["S","B","D","J","M","F","T","R"]
Stack8 = ["L","H","R","B","T","V","M"]
Stack9 = ["Q","P","D","S","V"]

STACKS = [Stack1,Stack2,Stack3,Stack4,Stack5,Stack6,Stack7,Stack8,Stack9]

for stackie in STACKS:
    print(stackie)

with open("Day 5.input") as file:
    Moves = [i for i in file.read().strip().split("\n")]

    for Move in Moves:
        countMoves = countMoves + 1
        print("===== ===== ===== ===== =====")
        print("Move Number    : ", countMoves)
        ExtractedMove = [i for i in Move.split(" ")]
        print("Amount To Move : ",ExtractedMove[1])
        print("From Stack     : ",ExtractedMove[3])
        print("To Stack       : ",ExtractedMove[5])
        # Add Item To Stack
        for i in range(int(ExtractedMove[1])):
            STACKS[int(ExtractedMove[5]) - 1].append(STACKS[int(ExtractedMove[3]) - 1][-1])
            STACKS[int(ExtractedMove[3]) - 1].pop()

            print(STACKS[int(ExtractedMove[3]) - 1])
            print()
    print("===== ===== ===== ===== =====")

for stackie in STACKS:
    print(stackie[-1])

print(Stack1[-1],Stack2[-1],Stack3[-1],Stack4[-1],Stack5[-1],Stack6[-1],Stack7[-1],Stack8[-1],Stack9[-1])

# Part Two
countMoves = 0
Stack1 = ["D","T","R","B","J","L","W","G"]
Stack2 = ["S","W","C"]
Stack3 = ["R","Z","T","M"]
Stack4 = ["D","T","C","H","S","P","V"]
Stack5 = ["G","P","T","L","D","Z"]
Stack6 = ["F","B","R","Z","J","Q","C","D"]
Stack7 = ["S","B","D","J","M","F","T","R"]
Stack8 = ["L","H","R","B","T","V","M"]
Stack9 = ["Q","P","D","S","V"]

STACKS = [Stack1,Stack2,Stack3,Stack4,Stack5,Stack6,Stack7,Stack8,Stack9]

with open("Input/Day 5") as file:
    Moves = [i for i in file.read().strip().split("\n")]
    for Move in Moves:
        countMoves = countMoves + 1
        print("===== ===== ===== ===== =====")
        print("Move Number    : ", countMoves)
        ExtractedMove = [i for i in Move.split(" ")]
        print("Amount To Move : ",ExtractedMove[1])
        print("From Stack     : ",ExtractedMove[3])
        print("To Stack       : ",ExtractedMove[5])
        # Add Item To Stack
        print("OLD STACK ",STACKS[int(ExtractedMove[5]) - 1])
        stringQ = []
        for i in range(int(ExtractedMove[1])):
            stringQ.append(STACKS[int(ExtractedMove[3]) - 1][-1])
            STACKS[int(ExtractedMove[3]) - 1].pop()
        print("StringQ        : ",stringQ)
        stringQ =  stringQ[::-1]
        print("StringQ        : ",stringQ)
        for Q in stringQ:
            print(Q)
            STACKS[int(ExtractedMove[5]) - 1].append(Q)
        print("NEW STACK",STACKS[int(ExtractedMove[5]) - 1])
        print()
    print("===== ===== ===== ===== =====")
for stackie in STACKS:
    print(stackie[-1])
print(Stack1[-1],Stack2[-1],Stack3[-1],Stack4[-1],Stack5[-1],Stack6[-1],Stack7[-1],Stack8[-1],Stack9[-1])