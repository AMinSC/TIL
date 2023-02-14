N = int(input()) # 26

f_n = N / 10 # 2
s_n = N % 10 # 6
new_n = f_n + s_n # 8
answer = (s_n * 10) + (new_n % 10) # 68
cnt = 1
while (N != answer): # 68 -> 84 -> 42
	f_n = s_n # 6 -> 8 -> 4
	s_n = answer % 10 # 8 -> 4 -> 2
	new_n = f_n + s_n # 14 -> 12 -> 6
	answer = (s_n * 10) + (new_n % 10) # 84 -> 42 -> 26
	cnt += 1

print(cnt)
