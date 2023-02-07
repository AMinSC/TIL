long long sum(int *a, int n)
{
	long long total = 0;
	int	i = 0;

	while (i < n)
	{
		total += a[i];
		i++;
	}
	return (total);
}
