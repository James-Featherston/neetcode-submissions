class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        temp = []

        def rec(start, summ):
            idx = start - 1
            while idx < len(candidates) - 1:
                idx += 1
                newSum = summ + candidates[idx]
                if newSum <= target:
                    temp.append(candidates[idx])
                    if newSum == target:
                        res.append(temp.copy())
                    else:
                        rec(idx + 1, newSum)
                    temp.pop()
                while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                    idx += 1
        rec(0, 0)
        return res
