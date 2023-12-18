class Solution {
    public boolean isPalindrome(int x) {
        String num = Integer.toString(x);
        if (x < 0) {
            return false;
        } else if (num.charAt(0) == '-') {
            return false;
        }
        int i = 0, j = num.length() - 1;
        while (i <= j) {
            if (num.charAt(i) != num.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}