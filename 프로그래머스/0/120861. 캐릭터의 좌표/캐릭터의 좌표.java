class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0, 0};
        int xMax = board[0] / 2;
        int yMax = board[1] / 2;
        
        for (String move: keyinput) {
            if (move.equals("left")) {
                if (answer[0] == xMax * -1) {
                    continue;
                } else {
                    answer[0] -= 1;
                }
            } else if (move.equals("right")) {
                if (answer[0] == xMax) {
                    continue;
                } else {
                    answer[0] += 1;
                }
            } else if (move.equals("up")) {
                if (answer[1] == yMax) {
                    continue;
                } else {
                    answer[1] += 1;
                }
            } else if (move.equals("down")) {
                if (answer[1] == yMax * -1) {
                    continue;
                } else {
                    answer[1] -= 1;
                }
            }
        }
        
        return answer;
    }
}