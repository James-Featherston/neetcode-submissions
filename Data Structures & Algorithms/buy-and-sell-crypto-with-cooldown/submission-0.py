class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def rec (bought, i):
            if i >= len(prices):
                return 0
            if (bought, i) in dp:
                return dp[bought, i]
            
            skip = rec(bought, i + 1)

            if not bought:
                buy = rec(True, i + 1) - prices[i]
                dp[(bought, i)] = max(buy, skip)
            else:
                sell = rec(False, i + 2) + prices[i]
                dp[(bought, i)] = max(sell, skip)
            return dp[(bought, i)]
        
        return rec(False, 0)


        