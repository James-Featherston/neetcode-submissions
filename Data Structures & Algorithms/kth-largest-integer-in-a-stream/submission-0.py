class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k

        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap,val)
        elif self.minheap[0] < val:
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
        return self.minheap[0]
        
