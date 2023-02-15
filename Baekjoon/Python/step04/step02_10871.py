cnt, fn = map(int, input().split())
num_list = list(map(int, input().split()))
for i in range(cnt):
	if fn > num_list[i]:
		print(num_list[i], end=" ")
