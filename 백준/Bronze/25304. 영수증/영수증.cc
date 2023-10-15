#include <stdio.h>

int main(void)
{
    int x, n, t=0;
    scanf("%d", &x);
    scanf("%d", &n);
    
    int a, b;
    for (int i = 1; i <= n; i++)
    {
        scanf("%d %d", &a, &b);
        a*=b;
        t+=a;
    }
    if (x==t) {printf("Yes\n");}
    else if (x!=t) {printf("No\n");}
    return 0;
}
