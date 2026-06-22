class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "fail";
        
        for (String[] user: db) {
            if (id_pw[0].equals(user[0])) {

                if (id_pw[1].equals(user[1])) {
                    return "login";
                } else {
                    return "wrong pw";
                }
            }
        }
        return answer;
    }
}