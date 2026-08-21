class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        dist = 0
        curr = 0
        steps = 0

        while dist < target:
            steps += 1
            nxt = dist + 1
            for i in range(curr, min(dist + 1, len(nums))):
                dist = max(dist, i + nums[i])
            curr = nxt
        return steps
        