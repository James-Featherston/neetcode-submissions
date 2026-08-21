class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            letters = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                letters[index] += 1
            if tuple(letters) not in m:
                m[tuple(letters)] = [s]
            else:
                m[tuple(letters)].append(s)
        res = []
        for key in m.keys():
            res.append(m[key])

        return res