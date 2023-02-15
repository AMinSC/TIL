answer = "O"
total_score = []
cnt = int(input())
for i in range(cnt):
	quiz = list(input().split())
	score = 0
	weight = 0
	for idx, val in enumerate(quiz):
		for sub_val in quiz[idx]:
			if answer == sub_val:
				weight += 1
				score += weight
			else:
				weight = 0
	total_score.append(score)
#	print(score) 답이지만 엔터를 해주지않으면 마지막 값이 나오지 않음
for i in total_score:
	print(i)
