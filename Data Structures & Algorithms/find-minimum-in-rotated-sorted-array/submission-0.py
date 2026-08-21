class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        small = nums[0]
        while l < r:
            m = (l + r) // 2
            if nums[l] > nums[m]:
                r = m - 1
                small = min(small, nums[m])
            else:
                l = m + 1
                small = min(small, nums[l])
        return small

        