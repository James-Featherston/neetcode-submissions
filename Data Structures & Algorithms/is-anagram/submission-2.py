class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for c in s:
            smap[c] = smap.get(c, 0) + 1
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        return smap == tmap