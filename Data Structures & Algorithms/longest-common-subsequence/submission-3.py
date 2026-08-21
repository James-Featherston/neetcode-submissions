class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #text1 is rows
        #text2 is cols
        ROWS, COLS = len(text1), len(text2)

        dp = [[0 for _ in range(COLS + 1)] for _ in range (ROWS + 1)]
        for row in range(1, ROWS + 1):
            for col in range(1, COLS + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        return dp[ROWS][COLS]