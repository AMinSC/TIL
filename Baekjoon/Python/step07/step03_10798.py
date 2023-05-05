board = []

for i in range(5):
    user_str = input()
    board.append(user_str)

max_len = max(len(val) for val in board)
test = []
for i in range(max_len):
    for j in range(5):
        try:
            test.append(board[j][i])
        except:
            pass

print(*test, sep="")
