exam = int(input())
exam_score = list(map(int, input().split()))
exam_max = max(exam_score)
for i in range(exam):
	exam_score[i] = exam_score[i] / exam_max * 100
print(sum(exam_score) / len(exam_score))
