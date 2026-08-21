class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                if nums[l] <= nums[m] and target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] >= nums[m] and target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
                    

    # 6, 1, 2, 3, 4, 5
        