// 백준 C언어로 다시 문제 풀기
// studing..

#include 	<stdio.h>
#include	<stdlib.h>

int	ans_check(char c, char b)
{
	if (c == b)
		return (1);
	return (0);
}

int	point_check(char *arr, char c)
{
	int	i = 0, total_point = 0, point = 0;

	while (arr[i])
	{
		if (ans_check(arr[i], c) && !ans_check(arr[i - 1], c))
		{
			point = 1;
			i++;
		}
		else if (ans_check(arr[i], c) && ans_check(arr[i - 1], c))
		{
			point++;
			i++;
		}
		while (arr[i] && !ans_check(arr[i], c))
			i++;
		total_point += point;
	}
	return (total_point);
}

int main(void)
{
	char answer[64];
	char ans = 'O';
	int	*ans_point;
	int	total_idx = 0, idx = 0;

	scanf("%d", &total_idx);
	ans_point = (int *)malloc(sizeof(int) * total_idx);
	if (!ans_point)
		return (0);

	while (idx < total_idx)
	{
		scanf("%s", answer);
		ans_point[idx] = point_check(answer, ans); // point_check func
		idx++;
	}
	idx = 0;
	while (idx < total_idx)
	{
		printf("%d\n", ans_point[idx]);
		idx++;
	}
}
