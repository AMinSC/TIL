using System;

public class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        double totalNumbers = 0;
        int numbersLen = numbers.Length;
        
        foreach (int num in numbers)
        {
            totalNumbers += num;
        }
        totalNumbers /= numbersLen;
        answer = Math.Round(totalNumbers, 1);
        
        return answer;
    }
}