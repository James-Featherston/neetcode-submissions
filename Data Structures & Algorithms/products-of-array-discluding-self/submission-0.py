class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1

        zero_count = 0

        for num in nums:
            if num != 0:
                product *= num
            if num == 0:
                zero_count += 1
        
        res = [0] * len(nums)

        if zero_count > 1:
            return res

        for idx, num in enumerate(nums):
            if num == 0:
                res[idx] = product
            elif zero_count == 1:
                res[idx] = 0
            else:
                res[idx] = math.floor(product / num)
        
        return res