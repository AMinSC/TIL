#include	<stdio.h>

int	n(int num)
{
	if (9 >= num)
		num += num;
	else if (1000 <= num)
		num = num + ((num / 1000) % 10) + ((num / 100) % 10) + ((num / 10) % 10) + (num %10);
	else if (100 <= num)
		num = num + ((num / 100) % 10) + ((num / 10) % 10) + (num % 10);
	else if (10 <= num)
		num = num + ((num / 10) % 10) + (num % 10);
	return (num);
}

int	main(void)
{
	int	arr[10001], selp_arr[10001]; // 10000번째 수까지 적용해야 되서 사이즈를 1 늘려줬다
	int	num = 10000, idx = 0, sub_idx = 0;

	while (idx <= num)
	{
		if (0 < idx)
			arr[idx] = n(idx);
		selp_arr[idx] = idx;
		idx++;
	}
	idx = 0;
	while (idx <= num)
	{
		sub_idx = 0;
		while (sub_idx <= num)
		{
			if (selp_arr[idx] == arr[sub_idx])
			{
				selp_arr[idx] = 0;
				break ;
			}
			sub_idx++;
		}
		idx++;
	}
	idx = 0;
	while (idx <= num)
	{
		if (0 < selp_arr[idx])
				printf("%d\n", selp_arr[idx]);
		idx++;
	}
}
