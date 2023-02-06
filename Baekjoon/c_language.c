// 백준 C언어로 다시 문제 풀기
// studing..

#include <stdio.h>
#include	<stdlib.h>

int main(void)
{
	float	*total_exam;
	float	answer = 0;
	int	cnt, exam, idx = 0, first_idx = 0, second_idx;

	scanf("%d", &cnt);
	total_exam = (float *)malloc(sizeof(float) * cnt);
	while (idx < cnt)
	{
		scanf("%d", &exam);
		total_exam[idx] = exam;
		idx++;
	}
	while (first_idx < cnt - 1)
	{
		second_idx = first_idx + 1;
		if (total_exam[first_idx] > total_exam[second_idx])
		{
			int	tmp;
			tmp = total_exam[first_idx];
			total_exam[first_idx] = total_exam[second_idx];
			total_exam[second_idx] = tmp;
		}
		first_idx++;
	}
	idx = 0;
	while (idx < cnt)
	{
		total_exam[idx] = total_exam[idx] / total_exam[cnt - 1] * 100;
		answer += total_exam[idx];
		idx++;
	}
	printf("%.4f\n", answer /= cnt); 
}
