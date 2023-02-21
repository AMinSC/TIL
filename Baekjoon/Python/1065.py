'''
문제를 잘못 인지하고 전전긍긍했던 문제
인지하지 못했던 문제 단어 "X의 각 자리가 등차수열"
문제 출제자의 의도는 101의 수는 1, 0, 1 이지만 인지하기 전에는 1~101 수 안의 등차수열 개수로 잘못 인지
'''
num = int(input())
cnt = 0
for i in range(1, num + 1):
	if 100 > i:
		cnt += 1
	elif 1000 > i:
		f_n = i // 100
		s_n = i // 10 % 10
		t_n = i % 10
		if s_n - f_n == t_n - s_n:
			cnt += 1
print(cnt)
