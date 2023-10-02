#include <stdio.h>

int main(void)
{
    int a;
    scanf("%d", &a);
    if (90 <= a)
    {
        printf("A\n");
    } else if (80 <= a)
    {
        printf("B\n");
    } else if (70 <= a)
    {
        printf("C\n");
    } else if (60 <= a)
    {
        printf("D\n");
    } else if (a < 60)
    {
        printf("F\n");
    }
    else
    {
        printf("error\n");
    }
    return 0;
}