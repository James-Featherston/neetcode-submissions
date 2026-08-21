class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + ":" + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        arr = []

        idx = 0

        while idx < len(s):
            right = idx
            while s[right] != ':':
                right += 1
            length = int(s[idx: right])
            idx = right + 1
            arr.append(s[idx: idx+length])
            idx = idx + length
        return arr

