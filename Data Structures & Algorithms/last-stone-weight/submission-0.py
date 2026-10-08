class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = []
        for stone in stones:
            heapq.heappush(minheap, -stone)

        while len(minheap) >= 2:
            stone1 = heapq.heappop(minheap) * -1
            stone2 = heapq.heappop(minheap) * -1
            if stone1 > stone2:
                heapq.heappush(minheap, stone2 - stone1)
            
        
        if len(minheap) > 0:
            return minheap[0] * -1
        return 0