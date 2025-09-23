class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=amount+1
        dp=[INF]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for x in coins:
                if i>=x:
                    dp[i]=min(dp[i],dp[i-x]+1)
        return -1 if dp[amount]==INF else dp[amount]