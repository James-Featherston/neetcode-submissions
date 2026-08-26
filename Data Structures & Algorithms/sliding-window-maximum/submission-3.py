class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        res = []

        if len(nums) == k:
            return [max(nums)]
        curMax = nums[0]
        curIdx = 0
        for i in range(k - 1):
            if nums[i] > curMax:
                curMax = nums[i]
                curIdx = i
            heapq.heappush(minHeap, (-nums[i], i))
        
        r =  k - 1
        while r < len(nums):
            heapq.heappush(minHeap, (-nums[r], r))
            if nums[r] > curMax:
                curMax = nums[r]
                curIdx = r
            while curIdx < r - k + 1:
                curMax, curIdx = heapq.heappop(minHeap)
                curMax = -curMax
            
            res.append(curMax)
            r += 1
        return res


