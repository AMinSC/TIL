def selp_num():
	s_num = []
	for i in range(10000):
		if 1000 <= i:
			s_num.append(i + (i // 1000 % 10) + (i // 100 % 10) + (i // 10 % 10) + (i % 10))
		elif 100 <= i:
			s_num.append(i + (i // 100) + (i // 10 % 10) + (i % 10))
		elif 10 <= i:
			s_num.append(i + (i // 10) + (i % 10))
		else:
			s_num.append(i + i)
	for i in range(10000):
		for j in s_num:
			if i == j:
				i = 0
		if 0 < i:
			print(i)

selp_num()
