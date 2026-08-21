class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        smallest = len(s)
        tmap = {}
        for char in t:
            tmap[char] = 1 + tmap.get(char, 0)
        
        smap = {}
        l, r = 0, 0
        smap[s[l]] = 1 + smap.get(s[l], 0)
        # for right in range
        while r < len(s):
            print(smap)
            if subset(tmap, smap):
                if smallest >= r - l + 1:
                    res = s[l:r + 1]
                    smallest = r - l + 1
                    print("setting smallest", res)
                smap[s[l]] -= 1 
                l += 1
            else:
                r += 1
                if r < len(s):
                    smap[s[r]] = 1 + smap.get(s[r], 0)
        return res
def subset(tmap, smap):
    for key in tmap:
        if key not in smap or smap[key] < tmap[key]:
            return False
    return True