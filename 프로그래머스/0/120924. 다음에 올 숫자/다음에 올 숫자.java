class Solution {
    public int solution(int[] common) {
        int answer = 0;
        int i = common.length - 1;
        int a = common[i]; int b = common[i - 1]; int c = common[i - 2];
        
        if ((a - b) == (b - c)) {
            answer = a + (b - c);
        } else {
            answer = a * (b / c);
        }
        return answer;
    }
}