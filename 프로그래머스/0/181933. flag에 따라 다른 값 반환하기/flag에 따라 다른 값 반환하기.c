#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, bool flag) {
    int answer = (flag) ? a + b : a - b;
    return answer;
}