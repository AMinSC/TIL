// 백준 C언어로 다시 문제 풀기

#include <stdio.h>

int main(void)
{
	int h, m;
	scanf("%d %d", &h, &m);
	
	int t, c = 0;
	scanf("%d", &t);

	m += t;

	if (m < 59)
	{
		printf("%d %d\n", h, m);
	}
	else if (m > 59)
	{
		while(m >= 60)
		{
			c++;
			m -= 60;
		}
		h += c;
		if (h > 23)
		{		
			h -= 23;
			printf("%d %d\n", h, m);
		}
		else if (h <= 23) 
		{
			printf("%d %d\n", h, m);
		}
	}
	return 0;
}

