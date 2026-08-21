class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {}

        for idx, num in enumerate(nums):
            if num in m:
                return [m[num], idx]
            m[target - num] = idx
