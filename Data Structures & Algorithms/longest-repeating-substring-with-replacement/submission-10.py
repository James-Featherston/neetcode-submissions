class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}

        l, r = 0, 0
        maxFreq = 0
        res = 0
        while r < len(s):
            c = s[r]
            hmap[c] = 1 + hmap.get(c, 0)
            maxFreq = max(maxFreq, hmap[c])

            if (r - l + 1) - maxFreq > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
            



        # ABABB

        