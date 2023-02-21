T = int(input())
answer = []
N = 0
while (N < T):
	answer.append(list(input()))
	N += 1
N = 0
while (N < T):
	print(answer[N][0], end='')
	print(answer[N][-1])
	N += 1
