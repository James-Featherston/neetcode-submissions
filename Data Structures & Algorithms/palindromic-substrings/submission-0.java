class Solution {
    public int countSubstrings(String s) {
        int length = s.length();
        int count = 0;
        for (int i = 0; i < length; i++) {
            count += helper(s, i, i, length);
            count += helper(s, i, i + 1, length);
        }
        return count;
        
    }

    public int helper(String s, int left, int right, int length) {
        int count = 0;
        if (right != length) {
            while (s.charAt(left) == s.charAt(right)) {
                count++;
                left--;
                right++;
                if (left < 0 || right >= length) {
                    break;
                }
            }
        }
        return count;
    }
}
