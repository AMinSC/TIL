#include	<stdio.h>

int	*selp_check(int *arr, int *check, int num)
{
	int	idx = 0, selp_idx = 0;
	while (idx <= num)
	{
		selp_idx = 0;
		while (selp_idx <= num)
		{
			if (check[idx] == arr[selp_idx])
				check[idx] = 0;
			selp_idx++;
		}
		idx++;
	}
	return (check);
}

void	selp_num(void)
{
	int	*answer;
	int	arr[10000], selp_arr[10000];
	int	num = 10000, idx = 1;

	while (idx <= num)
	{
		selp_arr[idx] = idx;
		idx++;
	}
	idx = 0;
	while (idx <= num)
	{
		int	selp = 0;
		if (9 >= idx)
			selp = idx + idx;
		else if (1000 <= idx)
			selp = idx + (idx / 1000) + ((idx / 100) % 10) + ((idx / 10) % 10) + (idx % 10);
		else if (100 <= idx)
			selp = idx + (idx / 100) + ((idx / 10) % 10) + (idx % 10);
		else if (10 <= idx)
			selp = idx + (idx / 10) + (idx % 10);
		arr[idx] = selp;
		idx++;
	}
	answer = selp_check(arr, selp_arr, num);
	idx = 0;
	while (idx <= num)
	{
		if (0 < answer[idx])
			printf("%d\n", answer[idx]);
		idx++;
	}
}

int main(void)
{
	selp_num();
}
