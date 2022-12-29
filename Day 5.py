#
# [M] [H]         [N]                
# [S] [W]         [F]     [W] [V]    
# [J] [J]         [B]     [S] [B] [F]
# [L] [F] [G]     [C]     [L] [N] [N]
# [V] [Z] [D]     [P] [W] [G] [F] [Z]
# [F] [D] [C] [S] [W] [M] [N] [H] [H]
# [N] [N] [R] [B] [Z] [R] [T] [T] [M]
# [R] [P] [W] [N] [M] [P] [R] [Q] [L]
#  1   2   3   4   5   6   7   8   9 

countMoves = 0

Stack1 = ["R","N","F","V","L","J","S","M"]
Stack2 = ["P","N","D","Z","F","J","W","H"]
Stack3 = ["W","R","C","D","G"]
Stack4 = ["N","B","S"]
Stack5 = ["M","Z","W","P","C","B","F","N"]
Stack6 = ["P","R","M","W"]
Stack7 = ["R","T","N","G","L","S","W"]
Stack8 = ["Q","T","H","F","N","B","V"]
Stack9 = ["L","M","H","Z","N","F"]

STACKS = [Stack1,Stack2,Stack3,Stack4,Stack5,Stack6,Stack7,Stack8,Stack9]

for stackie in STACKS:
    print(stackie)

with open("Day-5.in") as file:
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
