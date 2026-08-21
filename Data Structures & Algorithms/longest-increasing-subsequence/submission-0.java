class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] size = new int[nums.length];
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            size[i] = 1; 
            for (int j = i; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    size[i] = Math.max(size[i], size[j] + 1);
                }
            }
            max = Math.max(max, size[i]);
        }
        return max;
    }
}