T = int(input())
for i in range(T):
	arr = list(input().split())
	num = int(arr[0])
	s = arr[1]
	for j in range(len(s)):
		print(s[j] * num, end='')
	print()
