import java.util.Arrays;

class Solution {
    public int[][] solution(int[][] arr) {
        int arrLen = arr.length;
        int elLen = arr[0].length;
        
        if (arrLen > elLen) {
            for (int i = 0; i < arrLen; i++) {
                arr[i] = Arrays.copyOf(arr[i], arrLen);
            }
        } else if (arrLen < elLen) {
            int[][] newArr = new int[elLen][elLen];
            for (int i = 0; i < arrLen; i++) {
                newArr[i] = Arrays.copyOf(arr[i], elLen);
            }
            for (int i = arrLen; i < elLen; i++) {
                Arrays.fill(newArr[i], 0);
            }
            arr = newArr;
        }
        
        return arr;
    }
}