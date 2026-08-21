class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphaS = [0] * 26
        alphaT = [0] * 26

        for char in s:
            alphaS[ord(char) - ord('a')] += 1
        
        for char in t:
            alphaT[ord(char) - ord('a')] += 1
        
        return alphaS == alphaT