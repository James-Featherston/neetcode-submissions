class Solution {
    public boolean isPalindrome(String s) {
        String actualString = getActualString(s);
        for (int i = 0; i < (actualString.length())/2; i++) {
            if (actualString.charAt(i) != actualString.charAt(actualString.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    private String getActualString(String s) {
        StringBuilder result = new StringBuilder("");
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if ((curr >= 'a' && curr <= 'z') || 
                    (curr >= '0' && curr <= '9')) {
                result.append(curr);
            }
        }
        return result.toString();
    }
}