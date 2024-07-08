import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        Arrays.sort(array);

        int min = Math.abs(array[0] - n);
        int minIdx = 0;
        for(int i = 1; i < array.length; i++)
            if (Math.abs(array[i] - n) < min) {
                min = Math.abs(array[i] - n);
                minIdx = i;
            }

        return array[minIdx];
    }
}