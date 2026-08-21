class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = 0
            while s[i] != "#":
                num *= 10
                num += ord(s[i]) - ord("0")
                i += 1
            i += 1
            res.append(s[i: i+num]) 
            i += num
        return res

