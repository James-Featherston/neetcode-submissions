class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])

        prev = (0,intervals[0][0])
        res = 0
        for i in intervals:
            if prev[1] > i[0]:
                res += 1
                continue
            prev = i
        
        return res
        