board = [[0 for _ in range(101)] for _ in range(101)]

cnt = int(input())

for _ in range(cnt):
    x, y = map(int, input().split())
    for row in range(x, x+10):
        for col in range(y, y+10):
            board[row][col] = 1

print(sum(val.count(1) for val in board))
