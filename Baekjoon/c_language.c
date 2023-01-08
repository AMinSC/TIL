// 백준 C언어로 다시 문제 풀기
// studing..

#include <stdio.h>

int main(void)
{
	int a[32];
	for (int i = 0; i < 28; i++)
	{
		int n;
		scanf("%d", &n);
		a[n-1] = 1;
	}
	for (int i = 0; i < 30; i++)
	{
		if (a[i] == 0){printf("%d\n", i+1);}
	}
	return 0;
}

