class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)

        res = []
        prev = nums[0] + 1
        for i in range(0, len(nums) - 2):
            hset = set()
            if nums[i] == prev:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[r] + nums[l]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    if (nums[l], nums[r]) not in hset:
                        hset.add((nums[l], nums[r]))
                        res.append([nums[i], nums[l], nums[r]])
                    r-= 1
                    l+= 1
            prev = nums[i]
        return res

            