import java.util.Map;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public String solution(String s) {
        // 문자의 빈도를 저장할 맵
        Map<Character, Long> charCountMap = s.chars()
            .mapToObj(c -> (char) c)
            .collect(Collectors.groupingBy(c -> c, Collectors.counting()));

        // 빈도 1인 문자만 answer에 추가
        List<Character> answerList = charCountMap.entrySet().stream()
            .filter(entry -> entry.getValue() == 1)
            .map(Map.Entry::getKey)
            .sorted()
            .collect(Collectors.toList());

        // 빈도 1인 문자가 없으면 빈 문자열 반환
        if (answerList.isEmpty()) {
            return "";
        }

        // 리스트를 문자열로 변환하여 반환
        StringBuilder answer = new StringBuilder();
        for (char c : answerList) {
            answer.append(c);
        }

        return answer.toString();
    }
}