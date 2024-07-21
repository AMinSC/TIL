class Solution {
    public int solution(int M, int N) {
        int answer = 0;
        if (M == 1 && N == 1) {
            return answer;
        }
        
        
        return M * (N - 1) + (M - 1);
    }
}