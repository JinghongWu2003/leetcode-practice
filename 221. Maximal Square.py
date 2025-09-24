from typing import List


class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        best = 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if grid[i][0] == '1':
                dp[i][0] =1
                best=1
            else:
                dp[i][0] = 0
        for i in range(n):
            if grid[0][i] == '1':
                dp[0][i] = 1
                best=1
            else:
                dp[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                best = max(best, dp[i][j])
        return best * best

