class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        currSum = 0
        for num in nums:
            currSum += num
            maximum = max(maximum, currSum)
            if currSum < 0:
                currSum = 0
        return maximum