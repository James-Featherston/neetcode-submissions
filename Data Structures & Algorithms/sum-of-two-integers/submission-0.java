class Solution {
    public int getSum(int a, int b) {
        return sum(a, b);

    }
    private int sum(int a, int b) {
        if(a == 0 || b == 0) {
            return a|b;
        }
        return sum(a ^ b, (a & b) << 1);
    }
}
