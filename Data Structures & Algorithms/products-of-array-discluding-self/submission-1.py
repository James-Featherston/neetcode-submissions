class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                total *= num
        if zeroes > 1:
            return [0] * len(nums)
        
        res = []
        for num in nums:
            if zeroes:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total//num)
        return res