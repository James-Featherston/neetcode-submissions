class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        mini = r
        while l <= r:
            m = (r - l) // 2 + l
            
            total_hours = 0
            for pile in piles:
                total_hours += pile // m
                if pile % m != 0:
                    total_hours += 1
                
            if total_hours > h:
                l = m + 1
            elif total_hours <= h:
                r = m - 1
                mini = min(mini, m)
        return mini