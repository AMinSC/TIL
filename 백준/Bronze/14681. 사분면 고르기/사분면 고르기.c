#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    if (0 < a && 0 < b)
    {
        printf("1\n");
    } else if (0 > a && 0 < b)
    {
        printf("2\n");
    } else if (0 > a && 0 > b)
    {
        printf("3\n");
    } else if (0 < a && 0 > b)
    {
        printf("4\n");
    }
    else
    {
        printf("error\n");
    }
    return 0;
}
