class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort(key= lambda x: x[0])
        for curr in intervals:
            if not res:
                res.append(curr)
                continue
            prev = res[-1]
            if prev[1] >= curr[0]:
                if prev[1] < curr[1]:
                    res[-1] = [prev[0], curr[1]]
            else:
                res.append(curr)
        return res


        