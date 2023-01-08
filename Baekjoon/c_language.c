// 백준 C언어로 다시 문제 풀기
// studing..

#include <stdio.h>

int main(void)
{
	int a[16], b[16];
	for (int i = 0; i < 10; i++)
	{
		scanf("%d", &a[i]);
		b[i] = a[i] % 42;
	}

	int c = 0;
	for (int i = 0; i < 10; i++)
	{
		//printf("%d\n", b[i]);
		for (int j = i+1; j < 10; j++)
		{
			if (b[i] == b[j])
			{
				c++;
				break;
			}
		}
	}
	int d = c*2;
	int f = 10 - d;
	printf("\n\n");
	printf("%d\n", f+c);
	return 0;
}

