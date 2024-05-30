class Solution {
    public double solution(int[] numbers) {
        int num = 0;
        for (int n: numbers) {
            num += n;
        }
        return (float) num / numbers.length;
    }
}