class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        mini = r
        while l <= r:
            m = (r - l) // 2 + l
            
            count = 0
            for pile in piles:
                count += pile // m
                if pile % m != 0:
                    count += 1
                
            if count > h:
                l = m + 1
            elif count <= h:
                r = m - 1
                mini = min(mini, m)
        return mini