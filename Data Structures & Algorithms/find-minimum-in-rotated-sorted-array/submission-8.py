class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Case 1: target Less than mid and less than left = move l pointer right
        # Case 2: target Less than mid and greater than left = move r pointer l
        # Case 3: target Greater than mid and greater than right = move l pointer right
        # Case 4: Greater than mid and greater than right = move r pointer left
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r - l) // 2 + l
            if nums[m] >= nums[l] and nums[m] > nums[r]:
                l = m + 1
            elif nums[m] > nums[l] and nums[m] < nums[r]:
                r = m - 1
            elif nums[m] <= nums[l] and nums[m] < nums[r]:
                r = m

        return nums[r]