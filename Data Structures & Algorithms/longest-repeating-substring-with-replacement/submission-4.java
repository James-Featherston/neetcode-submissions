class Solution {
    public int characterReplacement(String s, int k) {
       int[] arr = new int[26];
       int ans = 0;
       int maxChar = 0;
       int left = 0;
       for (int right = 0; right < s.length(); right++) {
        arr[s.charAt(right) - 'A']++;
        maxChar = Math.max(maxChar, arr[s.charAt(right) - 'A']);
        if (right - left + 1 - maxChar > k) {
            arr[s.charAt(left) - 'A']--;
            left++;
        }
        ans = Math.max(ans, right - left + 1);
       }
       return ans;
    }
}
