class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()

        longest = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] in hs:
                hs.remove(s[l])
                l += 1
            else:
                longest = max(longest, r - l + 1)
                hs.add(s[r])
                r += 1
        return longest
                


        