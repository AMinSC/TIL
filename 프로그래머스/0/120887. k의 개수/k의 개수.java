import java.util.stream.IntStream;

class Solution {
    public long solution(int i, int j, int k) {
        return IntStream.rangeClosed(i, j)
                        .mapToObj(Integer::toString)
                        .flatMapToInt(String::chars)
                        .filter(c -> c == Integer.toString(k).charAt(0))
                        .count();
    }
}