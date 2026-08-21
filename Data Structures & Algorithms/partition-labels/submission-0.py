class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for num, c in enumerate(s):
            m[c] = num
        
        res = []
        size = 0
        begin = 0
        for num, c in enumerate(s):
            size = max(size, m[c] - begin + 1)
            if size + begin - 1 == num:
                res.append(size)
                size = 0
                begin = num + 1           
        return res