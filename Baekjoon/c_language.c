// 백준 C언어로 다시 문제 풀기

#include <stdio.h>

int main(void)
{
	int h, m;
	scanf("%d %d", &h, &m);

	if ( m > 45 ) { printf("%d %d\n", h, m-45);}
	else if ( m < 45) 
	{ 
		h -= 1;
		m += 15;
		if (0 > h) 
		{ 
			printf("%d %d\n", 23, m); 
		}
		else
		{
			printf("%d %d\n", h, m);
		}
	}
	return 0;
}

