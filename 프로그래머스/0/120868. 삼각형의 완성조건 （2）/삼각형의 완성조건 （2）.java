import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int solution(int[] sides) {
        int max = Arrays.stream(sides).max().getAsInt();
        int min = Arrays.stream(sides).min().getAsInt();
        int cnt = 0;
        
        long cnt1 = IntStream.range(max - min + 1, max + 1).count();
        long cnt2 = IntStream.range(max + 1, max + min).count();
        
        return (int)(cnt1 + cnt2);
    }
}