king = 1
queen = 1
rook = 2
bishop = 2
knight = 2
pawn = 8

chess = [king, queen, rook, bishop, knight, pawn]

for i in chess:
    find = int(input())
    print(f"{i - find}")