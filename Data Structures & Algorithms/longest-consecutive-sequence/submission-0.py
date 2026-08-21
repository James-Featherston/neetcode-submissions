class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        longest = 0

        for num in m:
            if num - 1 not in m:
                length = 1
                while (num + length) in m:
                    length += 1
                longest = max(length, longest)

        return longest
        