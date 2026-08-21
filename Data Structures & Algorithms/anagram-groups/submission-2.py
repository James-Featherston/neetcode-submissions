class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            currAlpha = [0] * 26
            for char in s:
                currAlpha[ord(char) - ord('a')] += 1
            if tuple(currAlpha) in m:
                m[tuple(currAlpha)].append(s)
            else:
                m[tuple(currAlpha)] = [s]
        
        res = []
        for val in m:
            res.append(m[val])
        return res