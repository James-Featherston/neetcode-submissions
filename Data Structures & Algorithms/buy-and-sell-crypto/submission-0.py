class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        currMin = prices[0]
        profit = 0

        for p in prices:
            currMin = min(p, currMin)
            profit = max(profit, p - currMin)
        
        return profit
        