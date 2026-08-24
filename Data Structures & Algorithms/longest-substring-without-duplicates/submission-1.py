class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()

        l, r = 0, 0
        maxi = 0

        while r < len(s):
            if s[r] in hset:
                while s[r] != s[l]:
                    hset.remove(s[l])
                    l += 1
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            maxi = max(maxi, r - l + 1)    
            r += 1
        return maxi

            
            
        