// 백준 C언어로 다시 문제 풀기
// studing.. 여러가지 코드 보기

#include <stdio.h>

int main(void)
{
	int n, c = 0;
	scanf("%d", &n);
	int a = n+1;
	if (n < 10) { n*=10; }
	int f, s;
	f = n / 10;
	s = n % 10;
	
	while(n != a)
	{
		a = f + s; // 8   14
		f = s; // 6  8
		if (a > 9) { s = a % 10; }
		else if (a <= 9) {s = a;} // 8  14
		a = (f*10) + s; // 68
		c++;
		f = a / 10; // 6
		s = a % 10; // 8
		//printf("%d %d %d\n", f, s, a);
	}
	printf("%d\n", c);
	
	return 0;
}

