n_class = int(input())
ans_list = []
for i in range(n_class):
	n_student = list(map(int, input().split()))
	avg_score = (sum(n_student) - n_student[0]) / n_student[0]
	avg_pass = 0
	for idx, val in enumerate(n_student):
		if 0 == idx:
			continue
		if avg_score < val:
			avg_pass += 1
	point = 100 / n_student[0]
	point *= avg_pass
	ans_list.append(point)
#print("{:.2f}%".format(avg_pass * n_student[0]))
for i in ans_list:
	print(f"{i:.3f}%")
