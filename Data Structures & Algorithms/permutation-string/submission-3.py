class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        rem = len(s1)
        m = [0] * 26

        for c in s1:
            i = ord(c) - ord("a")
            m[i] += 1
        
        l = 0
        r = 0
        curr = m.copy()
        while rem != 0 and r < len(s2):
            index = ord(s2[r]) - ord("a")
            if curr[index] > 0:
                curr[index] -= 1
                r += 1
                rem -= 1
            elif s2[l] == s2[r]:
                l += 1
                r += 1
            else:
                r += 1
                l = r
                curr = m.copy()
                rem = len(s1)
        
        if rem == 0:
            return True
        return False


            
