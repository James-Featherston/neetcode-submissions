class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)

        maxi = 0
        for num in nums:
            if num - 1 not in hset:
                i = num
                count = 0
                while i in hset:
                    count += 1
                    i += 1
                maxi = max(maxi, count)
        return maxi
