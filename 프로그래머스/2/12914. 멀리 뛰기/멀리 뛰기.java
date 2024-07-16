class Solution {
    public long solution(int n) {
        long answer = 1;
        long fibo = 0;
        
        for (int i = 0; i < n; i++) {
            long temp = answer;
            answer = (fibo + answer) % 1234567;
            fibo = temp;
            
        }
        
        return answer;
    }
}