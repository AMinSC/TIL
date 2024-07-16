import java.util.Arrays;

class Solution {
    public long solution(int[] array) {
        // 문자열로 변환 후, 문자 스트림으로 변환하여 '7' 문자 필터링 후 카운트
        return Arrays.stream(array)
            .mapToObj(Integer::toString)  // 각 정수를 문자열로 변환
            .flatMapToInt(String::chars)  // 각 문자열을 문자 스트림으로 변환
            .filter(c -> c == '7')        // 문자 '7'인 경우만 필터링
            .count();                     // 필터링된 문자의 개수를 카운트
    }
}
