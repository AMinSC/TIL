class Solution {
    public String[] solution(String[] quiz) {
        String[] result = new String[quiz.length];
        
        for (int i = 0; i < quiz.length; i++) {
            String[] strList = quiz[i].split(" ");
            int answer = Integer.parseInt(strList[0]) + (Integer.parseInt(strList[2]) * (strList[1].equals("+") ? 1 : -1));
            result[i] = (answer == Integer.parseInt(strList[4])) ? "O" : "X";
        }
        return result;
    }
}