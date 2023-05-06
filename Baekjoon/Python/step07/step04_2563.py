cnt = int(input())

total = cnt * 100
board = []
for i in range(cnt):
    paper = list(map(int, input().split()))
    board.append(paper)

a = list(sorted(board, key=lambda x: x[0], reverse=True))

f_idx = 0
s_idx = f_idx + 1
while s_idx < len(board):
    aa = a[f_idx][0] - a[s_idx][0]
    if aa < 10:
        row = 10 - aa
        if a[f_idx][1] > a[s_idx][1]:
            col = 10 - (a[f_idx][1] - a[s_idx][1])
        else:
            col = 10 - (a[s_idx][1] - a[f_idx][1])
    f_idx += 1
    s_idx += 1

print(total - row * col)
