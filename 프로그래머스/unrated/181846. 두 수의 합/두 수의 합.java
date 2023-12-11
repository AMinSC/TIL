import java.math.BigInteger;

class Solution {
    public String solution(String a, String b) {
        BigInteger numA = new BigInteger(a);
        BigInteger numB = new BigInteger(b);
        BigInteger sumNum = numA.add(numB);
        
        String answer = sumNum.toString();
        
        return answer;
    }
}