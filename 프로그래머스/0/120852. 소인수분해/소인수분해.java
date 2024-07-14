import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> solution(int n) {
        List<Integer> answer = new ArrayList<>();
        int startNum = 2;
        
        while (startNum <= n) {
            if (n % startNum == 0) {
                if (!answer.contains(startNum)) {
                    answer.add(startNum);
                }
                
                n /= startNum;
            } else {
                startNum++;
            }
        }
        return answer;
    }
}