N = int(input())
space = N
for i in range(N):
	print(("*" * (i + 1)).rjust(N))
'''
for i in range(N - 1, -1, -1):
	print(' ' * i + '*' * (N - i))
