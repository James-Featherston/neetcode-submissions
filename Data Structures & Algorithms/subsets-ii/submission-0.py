class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def rec (i):
            if i >= len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            rec(i + 1)
            temp.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            rec(i + 1)
        rec(0)
        return res
        