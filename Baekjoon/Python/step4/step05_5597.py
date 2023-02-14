s_num = list(map(int, input().split()))
s_num.sort()
t_num = list(range(1, 31))
for f_idx, f_val in enumerate(t_num):
	for s_idx, s_val in enumerate(s_num):
		if f_val == s_val:
			t_num[f_idx] = 0
	if 0 < t_num[f_idx]:
		print(t_num[f_idx])

