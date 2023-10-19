#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d", &t);
    int a[256], b[256];
    
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &a[i], &b[i]);
    }
    
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: %d + %d = %d\n", i + 1, a[i], b[i], a[i] + b[i]);
    }
    return 0;
}
