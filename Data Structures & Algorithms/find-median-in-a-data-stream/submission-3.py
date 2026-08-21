class MedianFinder:

    def __init__(self):
        self.isEven = True
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.isEven = not self.isEven
        l, r = 0, len(self.arr) - 1
        while l <= r:
            m = (l + r) // 2
            if num < self.arr[m]:
                r = m - 1
            elif num > self.arr[m]:
                l = m + 1
            else:
                l = m
                break
        self.arr.insert(l, num)

    def findMedian(self) -> float:
        m = len(self.arr) // 2
        if self.isEven:
            return (self.arr[m] + self.arr[m - 1]) / 2
        else:
            return self.arr[m]
        
        