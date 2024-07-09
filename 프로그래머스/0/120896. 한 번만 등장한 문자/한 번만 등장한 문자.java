import java.util.Map;
import java.util.HashMap;
import java.util.stream.Collectors;

class Solution {
    public String solution(String s) {
        // 문자의 빈도를 저장할 맵
        Map<Character, Integer> charCountMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCountMap.put(c, charCountMap.getOrDefault(c, 0) + 1);
        }

        // 빈도 1인 문자만 필터링하고 정렬하여 결과 문자열 생성
        String result = charCountMap.entrySet().stream()
            .filter(entry -> entry.getValue() == 1)
            .map(Map.Entry::getKey)
            .sorted()
            .map(String::valueOf)
            .collect(Collectors.joining());

        return result;
    }
}