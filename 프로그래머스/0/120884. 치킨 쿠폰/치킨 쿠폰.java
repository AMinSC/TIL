class Solution {
    public int solution(int coupon) {
        int order = 0; 
        while (coupon >= 10) {
            order += coupon / 10;
            int sub = coupon % 10;
            coupon = (coupon / 10) + sub;
        }
        
        return order;
    }
}