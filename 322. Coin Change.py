from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            imin=10001
            for x in coins:
                if i-x>=0 and dp[i-x]!=-1:
                    imin=min(imin,dp[i-x])
            dp[i]=imin+1 if imin!=10001 else -1
        return dp[amount]

print(Solution().coinChange([1,2,5], 11))