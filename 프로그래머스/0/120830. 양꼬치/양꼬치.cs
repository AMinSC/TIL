using System;

public class Solution {
    public int solution(int n, int k) {
        const int LambSkewers = 12000;
        const int Drink = 2000;
        int answer = 0;
        int serviceDrink = n / 10;
        
        answer = (LambSkewers * n) + (Drink * (k - serviceDrink));
        return answer;
    }
}