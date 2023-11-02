#include <stdio.h>

int black[] = {1, 1, 2, 2, 2, 8};

int main(void)
{
    int white[] = {0, 0, 0, 0, 0, 0};
    int count[] = {0, 0, 0, 0, 0, 0};
    scanf("%d %d %d %d %d %d", &white[0], &white[1], &white[2], &white[3], &white[4], &white[5]);
    
    for (int i = 0; i < 6; i++)
    {
        if (black[i] > white[i])
        {
            while(black[i] > white[i])
            {
                count[i]++;
                white[i]++;
            }
        } else if (black[i] < white[i])
        {
            while(black[i] < white[i])
            {
                count[i]--;
                white[i]--;
            }
        }
    }
    printf("%d %d %d %d %d %d\n", count[0], count[1], count[2], count[3], count[4], count[5]);
    return 0;
}

