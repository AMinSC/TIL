class Solution {
    public int solution(String A, String B) {
        String newB = B + B;
        int answer = (newB.contains(A)) ? newB.indexOf(A) : -1;
        return answer;
    }
}