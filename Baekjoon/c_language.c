// 백준 C언어로 다시 문제 풀기
// studing..

#include <stdio.h>

int main(void)
{
	int a[32];
	for (int i = 0; i < 28; i++)
	{
		scanf("%d", &a[i]);
	}
	int c=0;
	while(c < 28)
	{
	    for (int i = 0; i < 28; i++)
		{
			if (a[i] > a[i+1])
			{
				if (1<= a[i+1] & a[i+1] <= 30)
				{
					int b = a[i];
					a[i] = a[i+1];
					a[i+1] = b;
				}
			}
		}
		c++;
	}
	printf("\n\n");
	int b[32];
	for (int i = 0; i < 30; i++)
	{
		b[i] = i+1;
		for (int j = 0; j < 28; j++)
		{
			if (b[i] == a[j]) {b[i] = 0;}
		}
		if (b[i] > 0) {printf("%d\n", b[i]);}
	}
	return 0;
}

