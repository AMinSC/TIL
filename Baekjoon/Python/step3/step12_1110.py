N = int(input())

f_n = N // 10 # python에서 '/'은 나눗셈, "//"은 몫
s_n = N % 10
new_n = f_n + s_n
answer = (s_n * 10) + (new_n % 10)
cnt = 1
while (N != answer):
	f_n = s_n
	s_n = answer % 10
	new_n = f_n + s_n
	answer = (s_n * 10) + (new_n % 10)
	cnt += 1
print(cnt)
