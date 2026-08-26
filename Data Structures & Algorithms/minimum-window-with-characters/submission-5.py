class Solution:
    def minWindow(self, s: str, t: str) -> str:
        isValid = False
        res = ()
        minLen = len(s) + 1

        if len(t) > len(s):
            return ""

        # Use an array (52 chars) to find the occurances of the letters in s        
        def getIndex(c):
            if ord(c) >= ord("a") and ord(c) <= ord("z"):
                return ord(c) - ord("a")
            return 26 + ord(c) - ord("A")
        smap = [0] * 52
        tmap = [0] * 52
        # Fill the tmap for comparison

        for c in t:
            tmap[getIndex(c)] += 1
        r, l = 0, 0

        charsNeeded = len(t)
        charsFound = 0
        while r < len(s):
            # Go move right until find a valid solution
            c = s[r]
            smap[getIndex(c)] += 1
            # See if we found a char
            if smap[getIndex(c)] <= tmap[getIndex(c)]:
                charsFound += 1
            # See if we have a valid solution yet
            if not isValid and charsNeeded == charsFound:
                isValid = True
            
            # Check if we can move the left pointer and store result
            if isValid:
                while smap[getIndex(s[l])] > tmap[getIndex(s[l])]:
                    smap[getIndex(s[l])] -= 1
                    l += 1
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = (l, r)
            r += 1

        if isValid:
            return s[res[0]:(res[1] + 1)]
        return ""



        