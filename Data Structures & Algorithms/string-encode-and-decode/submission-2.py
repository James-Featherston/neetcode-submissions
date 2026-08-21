class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, s in enumerate(strs):
            strs[i] = str((1000 + len(s))) + s
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        idx = 0
        res = []
        while idx < len(s):
            letters = (ord(s[idx + 1]) - ord("0")) * 100 + (ord(s[idx + 2]) - ord("0")) * 10 + (ord(s[idx + 3]) - ord("0"))
            idx = idx + 4
            temp = []
            res.append(s[idx : idx + letters])
            idx = idx + letters
        return res

