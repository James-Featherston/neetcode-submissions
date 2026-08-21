class Solution {
    public int maxSubArray(int[] nums) {
        int right = 0;
        int left = 0;
        int max = nums[0];
        int total = 0;
        while (right < nums.length) {
            if (total < 0) {
                left = right;
                total = 0;
            }
            total += nums[right];
            max = Math.max(max, total);
            right++;

        }
        
        return max;
    }
}
