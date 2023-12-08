class Solution {
    public double solution(int[] numbers) {
        int num = 0;
        for (int n: numbers) {
            num += n;
        }
        return (double) num / numbers.length;
    }
}