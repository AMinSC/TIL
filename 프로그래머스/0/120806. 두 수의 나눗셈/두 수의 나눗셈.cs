using System;

public class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        double divVal = ((double)num1 / num2) * 1000;
        answer = (int)divVal;
        return answer;
    }
}