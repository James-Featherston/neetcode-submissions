class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a minheap that pops the bottom once above a freq
        # First need to count the freq

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        for num in freq:
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res