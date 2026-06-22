using System;

public class Solution {
    public int solution(int angle) {
        if (angle < 0 && angle > 181)
            return -1;
        const int RightAngle = 90;
        const int StraightAngle = 180;
        int answer = 0;
        
        if (RightAngle == angle)
        {
            return 2;
        }
        else if (StraightAngle == angle)
        {
            return 4;
        }
        else if (angle < 90)
        {
            return 1;
        }
        else
        {
            return 3;
        }
        
        return answer;
    }
}