// 백준 C언어로 다시 문제 풀기
// studing.. 여러가지 코드 보기

#include <stdio.h>

int main(void)
{
	int h, m;
	scanf("%d %d", &h, &m);
	
	int t, c = 0;
	scanf("%d", &t);

	t += m;

	if ( t <= 59)
	{
		printf("%d %d\n", h, t);
	}
	else if ( t > 59)
	{
		while(t > 59)
		{
			c++;
			t -= 60;
		}
		h += c;
		if (h > 23)
		{
			h -= 24;
			printf("%d %d\n", h, t);
		}
		else if (h <= 23)
		{
			printf("%d %d\n", h, t);
		}
	}
	return 0;
}

