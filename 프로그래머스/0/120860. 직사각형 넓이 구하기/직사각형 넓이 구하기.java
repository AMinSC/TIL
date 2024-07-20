import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        
        Arrays.sort(dots, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                if (a[0] != b[0]) {
                    return Integer.compare(a[0], b[0]);
                } else {
                    return Integer.compare(a[1], b[1]);
                }
            }
        });
        
        int x = Math.abs(dots[0][0] - dots[2][0]);
        int y = Math.abs(dots[0][1] - dots[1][1]);
        answer = x * y;
        
        return answer;
    }
}