// 백준 C언어로 다시 문제 풀기
// studing..

#include 	<stdio.h>

int main(void)
{
	double	total_score;
	int	class_num, exam_score, student, idx = 0, stud_idx, cnt = 0;

	scanf("%d", &class_num);
	double	class[class_num];
	while (idx < class_num)
	{
		scanf("%d", &student);
		int	student_score[student];
		stud_idx = 0;
		total_score = 0.0;
		while (stud_idx < student)
		{
			scanf("%d", &exam_score);
			student_score[stud_idx] = exam_score;
			total_score += exam_score;
			stud_idx++;
		}
		total_score /= student;
		stud_idx = 0;
		cnt = 0;
		while (stud_idx < student)
		{
			if (total_score < student_score[stud_idx])
				cnt++;
			stud_idx++;
		}
		class[idx] = (100 / (double)student) * cnt;
		idx++;
	}
	idx = 0;
	while (idx < class_num)
	{
		printf("%.3f%%\n", class[idx]);
		idx++;
	}
}
