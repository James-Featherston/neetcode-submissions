class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        PERMLEN = len(s1)

        s1arr = [0] * 26
        for c in s1:
            s1arr[ord(c) - ord('a')] += 1
        
        l, r = 0, 0
        s2arr = [0] * 26
        while l + PERMLEN - 1 < len(s2):
            c = s2[r]
            s2arr[ord(c) - ord("a")] += 1
            while s2arr[ord(c) - ord("a")] > s1arr[ord(c) - ord("a")]:
                s2arr[ord(s2[l]) - ord("a")] -= 1
                l += 1
            if r - l + 1 == PERMLEN:
                return True
            r += 1
        return False
