cnt = int(input())

board = []
row = 0
col = 0
for i in range(cnt):
    paper = list(map(int, input().split()))
    board.append(paper)

a = sorted(board, key=lambda x : x[0])
b = list(zip(*a))
print(f'board : {board}\na: {a}\nb: {b}\n')
