class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def rec(numsLeft):
            if not numsLeft:
                res.append(temp.copy())
                return
            for i in range(len(numsLeft)):
                temp.append(numsLeft[i])
                rec(numsLeft[:i] + numsLeft[i+1:])
                temp.pop()

        rec(nums)
        return res