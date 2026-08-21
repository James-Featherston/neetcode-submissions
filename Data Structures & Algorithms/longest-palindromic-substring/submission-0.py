class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        max_len = 0
        best = ""

        def rec(l, r, cur):
            if l < 0 or r >= size:
                return cur
            if s[r] == s[l]:
                return rec(l - 1, r + 1, cur + 2)
            return cur

        for i in range(len(s)):
            even_len = rec(i, i + 1, 0)
            odd_len = rec(i - 1, i + 1, 1)

            if even_len > max_len:
                max_len = even_len
                best = s[i - even_len//2 + 1: i + even_len//2 + 1]
            if odd_len > max_len:
                max_len = odd_len
                best = s[i - odd_len//2: i + odd_len//2 + 1]
        return best
        

        