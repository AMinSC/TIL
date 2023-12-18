class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        int maxNum = Math.max(denom1, denom2);
        int minNum = Math.min(denom1, denom2);
        if (maxNum % minNum == 0) {
            answer[0] = ((maxNum / minNum) * numer1) + numer2;
            answer[1] = maxNum;
        } else {
            answer[0] = (numer1 * denom2) + (numer2 * denom1);
            answer[1] = denom1 * denom2;
        }
        for (int i = answer[1]; i > 0; i--) {
            if (answer[0] % i == 0 && answer[1] % i == 0) {
                answer[0] /= i;
                answer[1] /= i;
            }
        }
        return answer;
    }
}