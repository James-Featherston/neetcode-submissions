class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if len(nums) <= k:
        #     return min(nums)
        arr = []
        def insertNum(num):
            if len(arr) == k:
                arr.pop(0)
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if num > arr[m]:
                    l = m + 1
                else:
                    r = m - 1
            arr.insert(l, num)
        i = 0
        for num in nums:
            if i < k:
                insertNum(num)
                i += 1
            elif num > arr[0]:
                insertNum(num)
        return arr[0]





        
        